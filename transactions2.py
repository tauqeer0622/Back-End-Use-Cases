import threading
import time
class Transaction:
    def __init__(self):
        self.lock=threading.Lock()
        self.wait_lock=threading.Lock()
        self.wait=0
        self.db={"student1":{"sid":"101","name":"tauqeer","balance":100},
                 "student2":{"sid":"102","name":"sangram","balance":200},
                 "student3":{"sid":"103","name":"harsha","balance":500},}
        self.pool_buffer={}
    def create(self,user):
        with self.lock:
            if user  in self.db:
                print("User already exists")
                return
            self.db[user]={}
            self.db[user]["sid"]=input(f"Enter student id of {user}: ")
            self.db[user]["name"]=input(f"Enter name of {user}: ")
            self.db[user]["balance"]=int(input(f"Enter amount of {user}: "))
            print()
            self.add(user)
    def select(self, user):
        if user not in self.db:
            print("User does not exist")
            return None
        return self.db[user]
    def update(self,user,bal):
        if user not in self.db:
            print("User does not exist in Database")
            return
        self.db[user]["balance"] = bal
        print("Wait For 3 sec to store in Database")
        time.sleep(3)
    def add(self,user):
        if user not in self.db:
            print("User does not exist in Database")
            return
        if user not in self.pool_buffer:
            self.pool_buffer[user]=self.db[user].copy()
            return
        print("user exists in Pool Buffer")
    def withdraw(self,user):
        status=self.lock.acquire(blocking=False)
        if  status:
            print(f"{threading.current_thread().name}Thread got the lock without waiting")
            print(threading.current_thread().name, "is working")
            print()
            try:
                res=self.withdraw2(user)
                if self.wait==0:
                    self.update(user,res)
            finally:
                self.lock.release()
                return
        with self.wait_lock:
            self.wait+=1
            print("Total Waiting Threads: ", self.wait)
        with self.lock:
            with self.wait_lock:
                self.wait-=1
                print("Total Waiting Threads 88: ",self.wait)
            print(threading.current_thread().name,"is working")
            res=self.withdraw2(user)
        if self.wait==0:
            self.update(user,res)
    def withdraw2(self,user):
            if user not in self.pool_buffer:
                print("User does not exist in Pool Buffer")
                return None
            amount=int(input(f"Enter amount to withdraw {user}: "))
            print()
            res=self.pool_buffer[user]
            if res["balance"] < amount:
                print("Insufficient Balance")
                return None
            res["balance"]-=amount
            return res["balance"]
    def display(self):
        print("DataBase",self.db)
        print("Pool Buffer :",self.pool_buffer)

obj=Transaction()
obj.add("student1")
obj.add("student2")
obj.add("student3")
# obj.display()
# # obj.add("student4")
t1=threading.Thread(target=obj.withdraw,args=("student1",))
t2=threading.Thread(target=obj.withdraw,args=("student1",))
t3=threading.Thread(target=obj.withdraw,args=("student1",))
t1.name="First Thread"
t2.name="Second Thread"
t3.name="Third Thread"
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
obj.display()