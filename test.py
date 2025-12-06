def sumop(a):
    def divop():
        y=a()
        return y//2
    return divop
@sumop
def display():
    return 50
# def mul(s):
#     return s ** 2
x=display()

print(x)
