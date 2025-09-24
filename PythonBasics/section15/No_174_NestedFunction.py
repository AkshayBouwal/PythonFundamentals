
def Outer():

    def inner():
        print("Inner Function")

    print("Outer Function")
    inner()

def totalArea(l, b, h):

    def area(d1, d2):
        return d1 * d2

    return 2 * (area(l, b) + area(l, h) + area(b, h))


if __name__ == '__main__' :

    #Outer()
    print(totalArea(1,2,3))















