s = "    Hello    "
x =s.lstrip()
print(x)

s = "$$$Hello2"
x =s.lstrip("$")
print(x)

s = "134Hello!!!!"
x =s.rstrip("!")
print(x)

s = "&&1Hello1&&"
x =s.strip("&")
print(x)

s = "#!Hel  lo$*"
x =s.strip("#!$*")
print(x)

