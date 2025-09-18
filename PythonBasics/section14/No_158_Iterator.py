# L1 = [5, 6, 10]
# iterator = iter(L1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# r = range(1,10)
# print(r)

def myrange(stop):
        i = 0
        while i < stop:
            yield i
            i += 1

m = myrange(5)
print(next(m))
print(next(m))
print(next(m))

def daygenerator():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    i = 0
    while True:
        if i > (len(days) - 1):
            i=0
        yield days[i]
        i += 1

n = daygenerator()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))














