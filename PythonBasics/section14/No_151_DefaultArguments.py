# l1 = [10, 20, 30, 40, 20, 50, 20]
# #if we don't pass anything then
# #default start = 0
# #default stop = length of string
# print(l1.index(20))
# print(l1.index(20,2))
# print(l1.index(20,2,4))

# def volume(l = 1, b = 2, h =3 ):
#     print(f"Length = {l}, Breadth = {b}, Height = {h}")
#     vol = l * b * h
#     return vol
#
# print(volume(10,5,4))
# print(volume(10,5))
# print(volume(10))
# print(volume())

def fun(l = [1,2,3]):
    l.append(len(l))
    print(l)

fun()
fun()
fun([10,12])
fun()
















