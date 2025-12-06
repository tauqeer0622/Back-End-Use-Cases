class PoolBuffer:
    def __init__(self):
        self.db={"student1":{"sid":"101","name":"tauqeer","percentage":65.78},
                 "student2":{"sid":"102","name":"sangram","percentage":70.80},
                 "student3":{"sid":"103","name":"harsha","percentage":50.66},}
        self.stack=[]
    def create(self,user):
        if self.read(user) in self.stack:
            self.stack.remove(self.read(user))
        if user not in self.db:
            self.db[user]={}
            self.db[user]["sid"]=input(f"Enter student id of {user}: ")
            self.db[user]["name"]=input(f"Enter name of {user}: ")
            self.db[user]["percentage"]=round(float(input(f"Enter percentage of {user}: ")),2)
            self.add(user)
        else:
            print("User already exists")
            return
    def read(self,user):
        if user not in self.db:
            print("User does not exist")
            return
        l=[]
        for i in self.db[user].values():
            l.append(i)
        return l
    def add(self,user):
        if self.read(user) not in self.stack:
            self.stack.append(self.read(user))
    def update(self,user):
        if user not in self.db:
            print("User does not exist")
            return
        self.db[user]["sid"] = input(f"Enter student id of {user}: ")
        self.db[user]["name"] = input(f"Enter name of {user}: ")
        self.db[user]["percentage"] = round(float(input(f"Enter percentage of {user}: ")), 2)
        if self.read(user) not in self.stack:
            self.read(self.db[user]["sid"])
    def delete(self,user):
        if user not in self.db:
            print("User does not exist")
            return
        if self.read(user) not in self.stack:
            self.add(user)
        self.stack.remove(self.read(user))
        self.db.pop(user)
    def display(self):
        print(self.db)
        print(self.stack)

obj=PoolBuffer()

# obj.display()
# print("="*20)
# obj.read("student1")
# obj.create("student1")
# obj.read("student")
# obj.update("student65")
# obj.delete("student1")
# obj.display()
# obj.add("student2")
# obj.display()

# print("="*20)
# obj.display()

