# l1 = [1, 2, 3, 4, 5]
# print(l1)
#
# #Take only one argument
# l1.append(6)
# print(l1)
#
# l2 = []
# l2.append(1)
# l2.append(2)
# l2.append(3)
# print(l2)
#
# #appending using slicing
# l2[len(l2):len(l2)] = [4]
# print(l2)

#######################################

# l1 = [1, 2, 3]
# l1.extend([4, 5, 6])
# print(l1)
#
# #using slicing
# l1[len(l1):len(l1)] = [7,8,9]
# print(l1)
#
# l1.extend("python")
# print(l1)
#
# #extend with range function
# l1.extend(range(10,15))
# print(l1)


####################################################

# l1 = [1,2,3,4]
# l1.insert(0,40)
# print(l1)
#
# #for any invalid index it will add to the end
# l1.insert(30, "Python")
# print(l1)

##################################################3

l1 = [1, 2, 3]
#shallow copy
l2 = l1.copy()
print(l2)

l1[1] = 5
print(l2)
print(l1)

















