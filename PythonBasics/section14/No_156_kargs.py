# def fun1(**keyVar):
#     print(keyVar)
#
# fun1(a=1,b=2,c=3)

def fun1(**keyVar):

    for key in keyVar:
        print(key)

    for value in keyVar.values():
        print(value)

fun1(a=1,b=2,c=3)


















