import threading
import time
class BookMyShow:
    def __init__(self):
        self.db={1:"Booked",2:"Available",3:"Available",
                 4:"Available",5:"Available",6:"Available",}
        self.pool_buffer={}
        self.wait=0
        self.lock=threading.Lock()
        self.wait_lock=threading.Lock()
    def show(self, seat):
        if seat not in self.pool_buffer:
            print(f"The item {seat} is not in the pool_buffer")
            return
        print(self.pool_buffer[seat])
    def add(self, seat):
        if seat not in self.db:
            print(f"The item {seat} is not in the database")
            return
        if seat not in self.pool_buffer:
            self.pool_buffer[seat]=self.db[seat]
            return
        print(f"The item {seat} is already added to the pool_buffer")
    def update(self,seat,new):
        if seat not in self.db:
            print(f"The seat {seat} is not in the database")
            return
        print("wait for update in Database")
        time.sleep(3)
        self.db[seat]=new

    def book2(self, seat):
        if seat not in self.pool_buffer:
            print(f"seat {seat} is not in the pool_buffer")
            return None

        if self.pool_buffer[seat] == "Booked":
            print(f"seat {seat} is already booked")
            return None
        print(threading.current_thread().name, "is working")
        time.sleep(3)
        self.pool_buffer[seat] = "Booked"
        print("Seat Booked Successfully by", threading.current_thread().name)
        return self.pool_buffer[seat]

    def book(self, seat):
        got = self.lock.acquire(blocking=False)
        if got:
            print(f"Thread {threading.current_thread().name} got the lock without waiting")
            try:
                self.book2(seat)
            finally:
                self.lock.release()
        else:
            with self.wait_lock:
                self.wait += 1
                print("Total Waiting Threads: ", self.wait)
            with self.lock:
                with self.wait_lock:
                    self.wait -= 1
                    print("Total Waiting Threads: ", self.wait)
                self.book2(seat)
    def cancel(self,seat):
        if seat not in self.pool_buffer:
            print(f"The item {seat} is not in the pool_buffer")
            return
        if self.pool_buffer[seat] == "Available":
            print(f"The item {seat} is already available")
            return
        self.pool_buffer[seat]="Available"
        ch=input("are you sure to cancel it?(yes/no) :")
        if ch=="yes":
            self.update(seat,self.pool_buffer[seat])
            print(f"Seat {seat} Canceled Successfully by", threading.current_thread().name)
        else:
            self.pool_buffer[seat]="Booked"
            print("Cancellation Failed")
    def display(self):
        print("DataBase :",self.db)
        print("Pool Buffer :",self.pool_buffer)

obj=BookMyShow()
for i in range(1,len(obj.db)+1):
    obj.add(i)
t1=threading.Thread(target=obj.book,args=(2,))
t2=threading.Thread(target=obj.book,args=(2,))
t3=threading.Thread(target=obj.book,args=(2,))
t1.name="First"
t2.name="Second"
t3.name="Third"
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
for seats,status in obj.pool_buffer.items():
    if obj.pool_buffer[seats]!=obj.db[seats]:
        obj.update(seats,status)
obj.display()
