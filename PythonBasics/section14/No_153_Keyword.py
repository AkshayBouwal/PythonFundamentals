def fun(a, b, *, c, d):
    print(a, b, c, d)


fun(a= 12, b= 23, c=35, d=42)
fun(13,  24, c=36, d=43)
#fun(13,  24, 36, d=43)