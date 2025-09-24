class Rectangle:

    # def __init__(self, l , b):
    #     self.length = l
    #     self.breadth = b

    def __init__(self, l = 1 , b = 1):
        print("self id:", id(self))
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

if __name__ == '__main__':

    rectangle2 = Rectangle(5)
    print("rectangle2 id:", id(rectangle2))
    print("Length:", rectangle2.length )
    print("Breadth:", rectangle2.breadth)
    print("Area:", rectangle2.area())
    print("Perimeter:",rectangle2.perimeter())

    # rectangle = Rectangle(15,8)
    # print("Length:", rectangle.length )
    # print("Breadth:", rectangle.breadth)
    # print("Area:", rectangle.area())
    # print("Perimeter:",rectangle.perimeter())

    # rectangle = Rectangle()
    # print("Length:", rectangle.length )
    # print("Breadth:", rectangle.breadth)
    # print("Area:", rectangle.area())
    # print("Perimeter:",rectangle.perimeter())

    # print("-" * 30)
    #
    # rectangle2 = Rectangle(5)
    # print("rectangle2 id:", id(rectangle2))
    # print("Length:", rectangle2.length )
    # print("Breadth:", rectangle2.breadth)
    # print("Area:", rectangle2.area())
    # print("Perimeter:",rectangle2.perimeter())