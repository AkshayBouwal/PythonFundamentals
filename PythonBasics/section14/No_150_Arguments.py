def volume(length, breadth, height):
    print(f"Length = {length}, Breadth = {breadth}, Height = {height}")
    vol = length * breadth * height
    return vol

#Positional Arguments
print(volume(15, 3, 4))

#Keyword Arguments
print(volume(length=10, breadth=11, height=12))

#Keyword Arguments - Order changed
#Can be passed in any order
print(volume(height=5, length=6, breadth=7))

#mixed argument
#But non keyword arguments should be corresponding to their position
#Otherwise Error
#Positional First then Keyword argument in case of mixed argument
print(volume(10, breadth=11, height=12))
