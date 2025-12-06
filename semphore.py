import time
import threading as th
import datetime
class Semaphore:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sumop(self):
        print(self.a+self.b)
    def div(self):
        print(self.a/self.b)
    def mul(self):
        print(self.a*self.b)
    def sub(self):
        print(self.a-self.b)
    def check_threaded(self,x):
        # print(x)
        start=datetime.datetime.now().second
        print("execution started at :",start)
        t1=th.Thread(target=x,args=())
        t1.start()
        time.sleep(8)
        end=datetime.datetime.now().second
        print("Execution ended at :",end)
        if (end-start) < 10:
            return True
        else:
            return False
obj=Semaphore(1,2)
# obj.sumop(1,2)
print(obj.check_threaded(obj.sumop()))