from itertools import permutations
a="abc"
s=permutations(a)
for i in s:
    print("".join(i))