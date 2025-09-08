#Single variable declaration and initialization
length = 15
print(length)

#List declaration and initialization
prices = [10,20,30,40,50]
print(prices)

#multiple variables of different datatypes
name, prices, qty = "Akshay", 12.25, 80
print(name, prices, qty)
print(id(name))

a,b,c = 1,1,1
print(a,b,c)
print(id(a), id(b), id(c))

d=e=f = 1
print(d,e,f)
print(id(d), id(e), id(f))