class Parent:

    def show(self):
        print('Parent method')


class Child(Parent):

    def show(self):
        print('Child method')


if __name__ == '__main__':
    c = Child()
    c.show()

    print(Child.mro())