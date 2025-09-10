a = 12
b = 54
c = 3

if a > b and a > c:
    print(str(a) + " is greatest number")
else:
    print(f"Either {b} is greater than {a} or {c} is greater than {a}")

if True or False:
    print("If condition is executed")
else:
    print("Else condition is executed")

if not True:
    print("Else condition is executed")
else:
    print("Else condition is executed")