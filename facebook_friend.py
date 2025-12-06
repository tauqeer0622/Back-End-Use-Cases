class Facebook_friend_rec:
    def __init__(self):
        self.graph={}
    def add_user(self,user):
        if user not in self.graph:
            self.graph[user]=[]
    def add_friend(self,user1,user2):
        self.add_user(user1)
        self.add_user(user2)
        if user2 not in self.graph[user1]:
            self.graph[user1].append(user2)
        if user1 not in user2:
            self.graph[user2].append(user1)
        return self.graph
    def suggestion(self,user):
        sug=set()
        for i in self.graph.get(user,[]):
            if i in self.graph:
                for j in self.graph.get(i,[]):
                    if user!=j :
                        sug.add(j)
        return sug
    def mutuals_suggestion(self,user1,user2):
        mutuals=set()
        for i in self.graph.get(user1,[]):
            if i in self.graph[user2]:
                mutuals.add(i)
        return mutuals
obj=Facebook_friend_rec()
obj.add_friend("a","b")
obj.add_friend("a","d")
obj.add_friend("b","c")
obj.add_friend("d","c")
# print("Mutuals : ",obj.mutuals_suggestion("d","b"))
print("Suggestions :",obj.suggestion("a"))
