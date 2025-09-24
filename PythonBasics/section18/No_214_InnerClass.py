class Outer:

    def __init__(self):
        self.in_obj = self.Inner()

    def show(self):
        self.in_obj.display()


    class Inner:

        def __init__(self):
            self.inner = "Inner Class Data"

        def display(self):
            print(self.inner)


if __name__ == '__main__':

    outer = Outer()
    outer.show()


