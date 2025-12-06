from itertools import permutations
class AutoCorrection:
    def __init__(self):
        self.d = {
            "apple": [],"banana": [],"orange": [],"grape": [],
            "mango": [],"water": [],"river": [],"mountain": [],
            "forest": [],"ocean": [],"sky": [],"cloud": [],"sun": [],
        }
        for i in self.d:
            perms = permutations(i)
            for j in perms:
                self.d[i].append("".join(j))
        print(self.d["apple"])
    def suggest(self,n):
        for i,j in self.d.items():
            if n in j:
                return i

    def display(self):
        return self.d
obj=AutoCorrection()
# print(obj.suggest("nabana"))

# print(obj.display())