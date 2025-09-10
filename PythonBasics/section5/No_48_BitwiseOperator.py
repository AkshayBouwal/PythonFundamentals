
a = 9

print(format(a,'b'))
print(a.bit_length())

print(a << 1)
print(a >> 1)

b = a

#b = 5

print(b is a)
print(a is b)


x = 35
y = 35

print(x is not y)