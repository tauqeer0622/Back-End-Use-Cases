import threading
import time
class Queue:
    def __init__(self,k):
        self.que=[]
        self.size=0
        self.cap=k
        self.lock=threading.Lock()
    def push(self,item):
        while True:
            with self.lock:
                if self.size<self.cap:
                    self.que.append(item)
                    self.size+=1
                    return
                print("Queue is full Wait For Release now you can consume")


    def pop(self):
        while True:
            with self.lock:
                if self.size>0:
                    self.que.pop()
                    self.size-=1
                    return
                print("Queue is empty Wait For Release")
                break
            time.sleep(1)
    def produce(self,item):
        for i in range(item):
            self.push(i)
            self.display()
    def consume(self,item):
        time.sleep(0)
        for i in range(item):
            self.pop()
            self.display()

    def display(self):
        print(self.que)

obj=Queue(5)
t1=threading.Thread(target=obj.produce,args=(8,))
t2=threading.Thread(target=obj.consume,args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
