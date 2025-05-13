print("decorator")
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

decorated_func = make_pretty(ordinary)
decorated_func()

print("@make_pretty")
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide ", a, " and ", b)
        if b == 0:
            print("You can't divide by zero")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a / b)

divide(2, 5)
divide(2, 0)

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner

def percentage(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner

@star
@percentage
def printer(msg):
    print(msg)

printer("Hello")
