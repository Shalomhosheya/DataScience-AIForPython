import math

def checkPositive(fun):
    def inner(number):
        if number < 0:
            print("Input must be a possitive numer : ")
        else:
            fun()
    return inner

@checkPositive
def calculate_squara_root(number):
    return math.sqrt(number)

print(calculate_squara_root(10))

