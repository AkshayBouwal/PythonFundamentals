# print(abs(-5))
# print(abs(6 + 8j))

# print(pow(2,10))
# print(pow(2,-2))
# #3rd argument is mode, it gives the result of (100 % 3  = 1)
# print(pow(10,2,3))

# print(round(4.6))
# print(round(4.5))
# print(round(5.5))
# # For 4.5 = 4 and For 5.5 = 6
# #Why
# #Banker's Rounding - Pick the nearest even number.
# print(round(3.54321))
# print(round(3.54321,2))


# print(divmod(10,3))

# print(min([10,64,41,52,74,25, -81]))
# print(min([10,64,41,52,74,25, -81] , key=abs))
# print(min([ ] , default="Empty List"))
# print(min([ ]))

# print(max(["apple", "banana", "cherry", "blueberry"], key=len))

# print(sum([1,2,3,4,5]))
# #initial value of sum = 10
# print(sum([1,2,3,4,5], start=10))

print(eval("10 + 20 * 4 - 5"))

global_dic = {"x":10, "y":15}
local_dic = {"z":3}
print(eval("x + y + z",global_dic,local_dic))


























