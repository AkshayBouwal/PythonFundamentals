class Rectangle:

    def __init__(self):
        self.length = 10
        self.breadth = 5

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

if __name__ == '__main__':

    rectangle = Rectangle()
    print("Length:", rectangle.length )
    print("Breadth:", rectangle.breadth)
    print("Area:", rectangle.area())
    print("Perimeter:",rectangle.perimeter())