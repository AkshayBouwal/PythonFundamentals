class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Cuboid(Rectangle):

    def __init__(self, l, b, height):
        self.height = height
        super().__init__(l, b)

    def volume(self):
        return self.length * self.breadth * self.height


if __name__ == '__main__':

    c1 = Cuboid(3,6,7)
    print(c1.volume())
