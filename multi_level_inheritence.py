class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display1(self):
        print("Name :",self.name)
        print("Age :" ,self.age)
class Student(Person):
    def __init__(self,name,age,roll_no,grades):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.grades=grades
    def display2(self):
        super().display1()
        print("roll No :",self.roll_no)
        print("Grades :",self.grades)
class GraduateStudent(Student):
    def __init__(self ,name,age,roll_no,grades,degree):
        super().__init__(name,age,roll_no,grades)
        self.degree=degree
    def display3(self):
        super().display2()
        print("Degree :",self.degree)
obj=GraduateStudent("tauqeer",27,66,"A","B.sc")
obj.display3()