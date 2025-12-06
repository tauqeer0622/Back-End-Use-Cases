class Stack:
    def __init__(self):
        self.stack=[]
class Browser_stack(Stack):
    def __init__(self):
        super().__init__()
    def push_url(self,value):
        self.stack.append(value)
    def pop_url(self):
        return self.stack.pop()
    def show_stack(self):
        print(self.stack)