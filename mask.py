import re
class Mask:
    def __init__(self):pass
    def email(self,email):
        self.e=email
        self.p=r"([a-zA-Z])([a-zA-Z0-9]+)(\@)([a-zA-Z0-9]+)(\.)([a-zA-Z]+)"
        self.match=re.search(self.p,self.e)
        self.match.group(2)
        self.match.group(3)
        self.match.group(4)
        self.match.group(5)
        self.match.group(6)
        return self.match.group(1)+(len(self.match.group(2))*"#")+self.match.group(3)+self.match.group(4)+self.match.group(5)+self.match.group(6)
    def phone(self,m):
        self.s=str(m)
        if self.s.isdigit():
            return ((len(self.s)-4)*"#")+self.s[-4:]
        else:
            return "Invalid Number"
    def aadhar(self,aadhar):
        self.a=str(aadhar)
        if self.a.isdigit():
            return self.a[:2]+((len(self.a)-2)*"#")+self.a[-2:]
        return "Invalid Aadhar Number"
obj=Mask()
print(obj.email("tauqeer0622@gmail.com"))
print(obj.phone(7028510622))
print(obj.aadhar(469826039098))
