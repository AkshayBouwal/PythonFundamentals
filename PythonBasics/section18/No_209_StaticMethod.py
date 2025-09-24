class Square:

    @staticmethod
    def calculate_area(length, breadth):
        area = length * breadth
        print(area)

if __name__ == '__main__':

    Square.calculate_area(15,15)