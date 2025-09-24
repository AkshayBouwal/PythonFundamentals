class Parent:

    def show(self):
        print("Parent Class - Show")


class Child(Parent):

    def show(self):
        #super().show()
        print("Child Class - Show")

if __name__ == '__main__':

    c = Child()
    c.show()