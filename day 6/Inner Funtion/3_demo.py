def make_pretty(fun):
    def inner():
        print("I got Decaretad")
        fun()
    return inner

@make_pretty
def odinary():
    print("I am Ordinary")

odinary()
