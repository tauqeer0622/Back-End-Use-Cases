class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,key,value):
        node = Node(key,value)
        if self.head is None:
            self.head=node
            self.tail=node
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
    def pop(self):
        if self.head is None:
            return None
        last=self.head
        self.head=self.head.next
        last.prev=None
        return last
    def display(self):
        if self.head is None:
            return None
        temp=self.head
        while temp:
            print(temp.key)
            print(temp.value)
            temp=temp.next
class  Stack(DoublyLinkedList):
    def __init__(self):
        self.stack=[]
        self.db = {0: {}, 1:{}}
        self.count = 0
        super().__init__()
    def push(self, key, value):
        super().push(key, value)
        if self.count%2 == 0:
            self.db[0][key]=value
        elif self.count %2== 1:
            self.db[1][key]=value

        self.count += 1
    def pop(self):
        super().pop()
    # def __init__(self):
    #     self.db={}
    #     super().__init__()
    # def push(self,key,value):
    #     super().push(key,value)
    #     self.db[key]=value
    # def pop(self):
    #     last=super().pop()
    #     self.db.pop(last)
    def display2(self):
        return self.db
obj=Stack()
# obj.display()
obj.push(1,"Man")
# obj.display()
obj.push(2,"Woman")
# obj.display()
obj.push(3,"Kid")
# obj.display()
# print(obj.display2())
obj.push(4,"Child")
obj.display()
print(obj.display2())
obj.pop()
print("="*50)
print("After Pop")
print(obj.display2())
obj.display()



