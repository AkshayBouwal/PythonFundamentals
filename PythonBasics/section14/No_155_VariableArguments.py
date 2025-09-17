# print(10, 12.5, "Hello", 5, True)

# def fun(*arguments):
#     print(arguments)
#
# fun(5)
# fun(5,10)
# fun(5,10,15)
# fun(5,"Hello",True)


# def fun(*arguments):
#
#     for x in arguments:
#         if type(x) == int:
#             print(x)
#
#
# fun(5,"Hello",True, 15)

# def fun(a, b, *arguments):
#     print(a)
#     print(b)
#     print(arguments)
#     #* unpack the tuple
#     print(*arguments)
#
# fun(5,"Hello",True, 15)

def fun(*arguments):
    print(arguments,len(arguments))

fun([1,2,3,4,5])
fun(*[1,2,3,4,5])






















