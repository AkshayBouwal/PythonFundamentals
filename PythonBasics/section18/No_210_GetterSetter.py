class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):

        if length >= 0:
            self._length = length
        else:
            self._length = 1


    def area(self):
        return self.length * self.width



if __name__ == '__main__':

    r1 = Rectangle(10,5)
    r1.length = -10
    print(r1.area())


