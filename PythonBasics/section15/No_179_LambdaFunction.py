def double(x):
    return x * 2

k = lambda x: x * 2

add = lambda x, y: x + y

def filterFunction():
    l1 = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]

    f = filter(lambda x: x % 3 == 0, l1)
    l2 = list(f)
    print(l2)

def mapFunction():

    l1 = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
    f = map(lambda x: x * x, l1)
    l2 = list(f)
    print(l2)

def conditional():

    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = map(lambda x: x if x % 2 == 0 else 0, l1)
    l2 = list(k)
    print(l2)


if __name__ == '__main__':
    # print(double(3))
    # print(k(6))
    # print(add(3,9))
    #
    # print((lambda x,y: x - y)(30,12))

    # filterFunction()
    #mapFunction()

    conditional()
