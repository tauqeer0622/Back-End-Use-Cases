class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}     # key → value
        self.order = []     # keeps track of usage order (MRU at end)

    def get(self, key):
        if key not in self.cache:
            return -1

        # move key to most recently used position
        self.order.remove(key)
        self.order.append(key)

        return self.cache[key]

    def put(self, key, value):
        # if key already exists, update and move to MRU
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
            return

        # if cache is full → remove LRU
        if len(self.cache) == self.capacity:
            lru = self.order.pop(0)  # first element = least recently used
            del self.cache[lru]

        # insert new key
        self.cache[key] = value
        self.order.append(key)

    def __repr__(self):
        return f"LRU Order: {self.order} | Cache: {self.cache}"
cache = LRUCache(3)

cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
print(cache)  # [1,2,3]

# cache.get(2)
# print(cache)  # [1,3,2]  (2 became MRU)
#
# cache.put(4, "D")  # removes 1 (LRU)
# print(cache)  # [3,2,4]
