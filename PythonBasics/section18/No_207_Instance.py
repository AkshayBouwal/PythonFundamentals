class Rectangle:

    def __init__(self, l = 1 , b = 1):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

if __name__ == '__main__':

    r1 = Rectangle()