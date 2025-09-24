class Rectangle:

    count = 0

    def area(self):
        return self.length * self.breadth

    def __init__(self, l = 1 , b = 1):
        self.length = l
        self.breadth = b
        Rectangle.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


if __name__ == '__main__':

    r1 = Rectangle(1,2)
    r2 = Rectangle(3,6)
    print(Rectangle.get_count())



    # r1 = Rectangle(1,2)
    # print(Rectangle.count)
    #
    # r2 = Rectangle(3,6)
    # print(Rectangle.count)
    #
    # r3 = Rectangle(5,5)
    # print(Rectangle.count)