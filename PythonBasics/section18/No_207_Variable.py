class Variable:

    def __init__(self):
        self.a = 10
        self.fun()

    def fun(self):
        self.b = 20

    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)


if __name__ == '__main__':
    obj1 = Variable()
    obj1.c = 30
    obj1.show()

