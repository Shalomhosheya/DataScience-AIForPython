def outer(x):
    def inner(y):
        return x+y 
    return inner

funtion = outer(5)
print(funtion)
print(funtion(10))
print(outer(5)(10))


def add(x,y):
    return x + y

def calculate(funtion,x,y):
    return funtion(x,y)

resualt = calculate(add,10,10)

print(resualt)
