import threading
import time
class Database:
    def __init__(self):
        self.lock=threading.Lock()
        self.db={"student1":{"sid":"101","name":"tauqeer","percentage":65.78},
                 "student2":{"sid":"102","name":"sangram","percentage":70.80},
                 "student3":{"sid":"103","name":"harsha","percentage":50.66},}
        self.pool_buffer=[]
    def create(self,user):
        with self.lock:
            if user  in self.db:
                print("User already exists")
                return
            self.db[user]={}
            self.db[user]["sid"]=input(f"Enter student id of {user}: ")
            self.db[user]["name"]=input(f"Enter name of {user}: ")
            self.db[user]["percentage"]=round(float(input(f"Enter percentage of {user}: ")),2)
            print()
            self.add(user)
    def select(self, user):
        if user not in self.db:
            print("User does not exist")
            return
        for i,j in self.db[user].items():
            print(f"{i}:{j}")
    def update(self,user):
        with self.lock:
            if user not in self.db:
                print("User does not exist")
                return
            print(threading.current_thread().name)
            self.db[user]["sid"] = input(f"Enter student id of {user}: ")
            self.db[user]["name"] = input(f"Enter name of {user}: ")
            self.db[user]["percentage"] = round(float(input(f"Enter percentage of {user}: ")), 2)
            print("Wait For 5 sec")
            time.sleep(5)

    def delete(self,user):
        with self.lock:
            if user not in self.db:
                print("User does not exist")
                return
            self.pool_buffer.remove(self.db[user])
            self.db.pop(user)
    def add(self,user):
        if user not in self.db:
            print("User does not exist")
            return
        self.pool_buffer.append(self.db[user])
    def display(self):
        print("DataBase",self.db)
        print("Pool Buffer :",self.pool_buffer)

obj=Database()
obj.add("student1")
obj.add("student2")
obj.add("student3")
# obj.display()

t1=threading.Thread(target=obj.update,args=("student1",))
t2=threading.Thread(target=obj.update,args=("student1",))
t1.name="First Thread"
t2.name="Second Thread"
t1.start()
t2.start()
t1.join()
t2.join()




