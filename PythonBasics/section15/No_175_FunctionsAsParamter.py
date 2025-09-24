def welcome():
    print('Welcome to Python Basics')

def fun(f):
    f()

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def arithemetic(f,a,b):
    return f(a,b)

if __name__ == '__main__':

    # fun(welcome)

    out = arithemetic(add, 50,25)
    print(out)












    