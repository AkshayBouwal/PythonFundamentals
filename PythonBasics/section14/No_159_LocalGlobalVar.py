# g = 5.25
# print("Outside - 1:", g)
#
# def fun():
#     global g
#     a = 10
#     g = 199
#     print("Variable a", a)
#     print("Variable g", g)
#
# fun()
# print("Update Global Variable:" ,g)


x, y,z = 1, 2.324, "Hello"

def func():
    a, b, c = 1, 2, 3
    print(locals())
    print(globals())


func()


















