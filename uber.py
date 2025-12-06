import heapq
class Uber:
    def __init__(self):
        self.graph={'A' : {'B':1,'C':9},
                    'B' : {'A': 1, 'C': 4,'E': 7,},
                    'C' : {'A':9,'B':4,'E':3,'D':8},
                    'D' : {'C':8,'E':6,'F':5},
                    'E' : {'B':7,'C':3,'D':6,'F':2},
                    'F' : {'E':2,'D':5}}
        self.distances={i:float('inf') for i in self.graph}
        self.previous={i:None for i in self.graph}
    def get_distance(self,start):
        self.que=[(0,start)]
        while self.que:
            weight,node=self.que.pop(0)
            if weight>self.distances[node]:
                continue
            for i,j in self.graph[node].items():
                distance=weight+j
                if distance<self.distances[i]:
                    self.distances[i]=distance
                    self.previous[i]=node
                    heapq.heappush(self.que,(distance,i))
        return self.distances,self.previous

    def get_path(self,start,end):
        self.get_distance(start)
        path=[]
        s=end
        while s!=start:
            path.append(s)
            s=self.previous[s]
        path.append(start)
        return path[::-1]
    def display(self):
        print(self.distances)
        print("="*40)
        print(self.previous)
obj=Uber()
print(obj.get_path("A","E"))
obj.get_distance('A')
obj.display()
