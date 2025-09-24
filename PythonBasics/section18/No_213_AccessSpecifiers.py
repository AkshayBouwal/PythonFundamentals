class Parent:

    def __init__(self, d):
        self._data = d

    def show(self):
        print(self._data)

class Child(Parent):

    def __init__(self, d):
        super().__init__(d)

    def display(self):
        print(self._data)



if __name__ == '__main__':

    child = Child(25)
    child.show()
    child.display()









    # p = Parent(2)
    # p.show()
    #
    # #Name Mangling
    # p._Parent__data = 15
    # p.show()

    # p.__data = 15
    # p.show()

