class Queue:
    def __init__(self,k):
        self.que=[0]*k
        self.stack=[0]*k
        self.stack_front=0
        self.stack_rear=0
        self.stack_size=0
        self.que_front=0
        self.que_rear=0
        self.que_size=0
        self.cap=k
    def enque(self,val):
        if self.is_full():
            print("Que is Full")
            return
        self.que[self.que_rear]=val
        self.que_rear=(self.que_rear+1)%self.cap
        self.que_size+=1
    def deque(self):
        if self.is_empty():
            print("Que is empty")
            return
        self.stack[self.stack_rear]=self.que[self.que_front]
        self.stack_rear=(self.stack_rear+1)%self.cap
        self.stack_size+=1
        self.que[self.que_front]=None
        self.que_front=(self.que_front+1)%self.cap
        self.que_size-=1

    def is_full(self):
        return self.que_size==self.cap
    def is_empty(self):
        return self.que_size==0
    def display(self):
        print("Que :",self.que)
        print("stack :",self.stack)
obj=Queue(5)
for i in [10,20,30,40,50,60]:
    obj.enque(i)
obj.display()
obj.deque()
obj.display()
obj.deque()
obj.display()
obj.deque()
obj.display()
obj.deque()
obj.display()
obj.deque()
obj.display()
obj.deque()
obj.display()
obj.deque()
obj.display()
obj.enque(60)
obj.display()
obj.enque(70)
obj.display()
obj.deque()
obj.display()


