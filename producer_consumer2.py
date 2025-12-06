import threading


class Queue:
    def __init__(self, capacity):
        self.que = []
        self.cap = capacity
        self.front=0
        self.rear=capacity-1
        self.size=0
        self.p=threading.Lock()
        self.c=threading.Lock()
        if self.isempty():
            self.p.acquire()
            self.c.release()
        elif self.isfull():
            self.p.release()
            self.c.acquire()
    def enque(self, item):
        self.que.pop()
        self.que.append(item)
        self.size += 1
    def deque(self):
        if self.isempty():
            return None
        self.que[self.rear]=None
        self.rear=(self.rear-1)%self.cap
        return self.que[self.rear]
    def isempty(self):
        return self.rear==self.cap-1
    def isfull(self):
        return self.size == self.cap
    def display(self):
        return self.que
class Producer(Queue):
    def __init__(self,capacity):
        super().__init__(capacity)
    def push(self,item):
        if self.isfull():
            print("Queue is Full")
            return
        elif not self.isempty():
            print("There are some values in the queue")
            return
        super().enque(item)
class Consumer(Queue):
    def pop(self):
        if self.isempty():
            print("Queue is Empty")
            return
        super().deque()
obj=Producer(5)
print(obj.display())
# obj.enque(1)
# obj.enque(2)
for i in [1,2,3,4,5]:
    obj.push(i)
obj2=Consumer(5)
print(obj.display())
for i in range(5):
    obj2.pop()
print(obj.display())