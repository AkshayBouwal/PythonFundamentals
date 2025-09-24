# def Outer():
#     msg = "Welcome"
#
#     def Inner():
#         print("+" * 10)
#         print(msg)
#         print("+" * 10)
#
#     return Inner()

def get_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

if __name__ == "__main__":

    # f = Outer
    # f()

    c1 = get_counter()
    c2 = get_counter()

    print(c1(), c1(), c1())
    print(c2(), c2(), c2())







    