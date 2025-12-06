import time
def try_book_seats(user_id, bus_id, date, requested_seat_ids, idempotency_key):
    # 1) Check idempotency store
    if idempotency_store.exists(idempotency_key):
        return idempotency_store.get(idempotency_key)

    now = time.monotonic()

    # 2) Attempt to mark seats as HOLD using optimistic locking
    # Begin DB transaction
    existing = db.query("SELECT seat_id, state, version FROM seat_inventory WHERE seat_id IN (...) AND date = ? FOR UPDATE", ...)
    for row in existing:
        if row.state != 'AVAILABLE':
            raise SeatUnavailableError()

    # Set hold record
    hold_id = create_hold_record(user_id, requested_seat_ids, expires_at = now + HOLD_TTL)
    for seat in requested_seat_ids:
        # update seat state and bump version
        updated = db.execute(
            "UPDATE seat_inventory SET state='HOLD', hold_id=?, version=version+1 WHERE seat_id=? AND date=? AND state='AVAILABLE'",
            (hold_id, seat, date)
        )
        if updated == 0:
            # someone else grabbed it — rollback and fail
            db.rollback()
            raise SeatUnavailableError()

    db.commit()
    # Put brief entry in Redis cache for fast reads
    redis.hset(f"bus:{bus_id}:{date}", mapping={seat:'HOLD' for seat in requested_seat_ids})
    # Save idempotency result
    idempotency_store.set(idempotency_key, {"status":"HOLD", "hold_id":hold_id}, ttl=HOLD_TTL)
    return {"status":"HOLD", "hold_id":hold_id}
