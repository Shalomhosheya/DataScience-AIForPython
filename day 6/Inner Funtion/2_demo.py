def make_pretty(fun):
    def inner():
        print("I got Decaretad")
        fun()
    return inner

def odinary():
    print("I am Ordinary")

resualt = make_pretty(odinary)
resualt()