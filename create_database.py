class Database:
    def __init__(self):
        self.db={}
        self.count=1
    def insert(self,record):
        pk=self.count
        self.db[pk]=record
        self.count+=1
        return self.db
    def update(self,key,record):
        if key in self.db:
            self.db[key]=record
    def remove(self,key):
        if key in self.db:
            del self.db[key]
    def select(self):
        return self.db

obj=Database()
obj.insert([1,2,3,4])
obj.insert([5,6,7,8])
obj.update(6,[7,8])
print(obj.select())



