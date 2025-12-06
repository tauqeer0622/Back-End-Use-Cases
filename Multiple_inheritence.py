class Academic:
    def __init__(self,grades,subject):
        self.grade=grades
        self.subject=subject
    def display1(self):
        print("Grades :",self.grade)
        print("Subject",self.subject)
class Extracurricular:
    def __init__(self,act,awards):
        self.act=act
        self.awards=awards
    def display2(self):
        print("Activity :",self.act)
        print("Awards :",self.awards)
class Student(Academic,Extracurricular):
    def __init__(self,grades,subject,act,awards):
        Academic.__init__(self,grades,subject)
        Extracurricular.__init__(self,act,awards)
    def display3(self):
        # Academic.display1(self)
        super().display1()
        super().display2()
obj=Student("a","Math","Reading","POTM")
obj.display3()