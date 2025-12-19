#Scope example
n=2
def trial(num):
    return num ** n

print(trial(2))

#closure example

def fun(num):
    def fun1(n):
        return num **n
    return fun1

f=fun(2)
print(f(3))

