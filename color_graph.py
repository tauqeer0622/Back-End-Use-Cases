class Color:
    def __init__(self):
        self.graph={"a":{"b","d"},"b":{"a","c"},"c":{"b","d"},"d":{"a","c"}}
        self.nodes=[i for i in self.graph]
        self.count=0
        self.color={}
    def get_count(self):
        for node in self.nodes:
            if node in self.color:
                continue
            self.count+=1
            self.color[node]=self.count
            for j in self.nodes:
                if j in self.color:
                    continue
                res=True
                for neighbor in self.graph[j]:
                    if self.color.get(neighbor)==self.count:
                        res=False
                        break
                if res:
                    self.color[j]=self.count
        return self.color,self.count
    def display(self):
        print(self.graph)
        print(self.nodes)

obj=Color()
# obj.get_count()
# obj.get_count().
# obj.display()
obj.get_count()
print(obj.color)
print("Minimum Color Count :",obj.count)
