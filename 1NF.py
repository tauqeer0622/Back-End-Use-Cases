import pandas as pd
class DatabBase:
    def __init__(self):
        self.db={1:{"name":"Tauqeer","No":[7028,5106]},
                 2:{"name":"uzair","No":[9673,7563]},
                 3:{"name":"harsha","No":[9035,9795]}}
        self.n=[]
    def add(self):
        for i,j in self.db.items():
            i_d=i
            name=j["name"]
            no_list=j["No"]
            for r in no_list:
                no=r
                self.n.append({"id":i_d,"name":name,"no":no})
    def display(self):
        print("Database :",self.db)
        print("1N :",self.n)
obj=DatabBase()
obj.display()
obj.add()
obj.display()
df=pd.DataFrame(obj.db)
print(df)