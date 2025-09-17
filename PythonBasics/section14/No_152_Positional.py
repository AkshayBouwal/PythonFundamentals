def fun(a, b, /, c, d):
    print(a, b, c, d)


fun(10, 20, 30, 40)
fun(12, 23, c=35, d=42)
#fun(a=24, b=25, c=37, d=47)
