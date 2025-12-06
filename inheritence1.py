class Student:
    def __init__(self,sid,sname):
        self.sid=sid
        self.sname=sname
    def display1(self):
        print("Student ID :",self.sid)
        print("Student Name :",self.sname)
class Graduate(Student):
    def __init__(self,sid,sname,degree,per):
        super().__init__(sid,sname)
        self.deg=degree
        self.per=per
    def display2(self):
        super().display1()
        print("Degree :",self.deg)
        print("Percentage :",self.per)
obj=Graduate(101,"Tauqeer","B.sc",79.88)
obj.display2()