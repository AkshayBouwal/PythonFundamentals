# l1 = [1, 2, 3]
# l2 = [8, 9, 10]
#
# l3 = l1 + l2
# print(l3)
#
# #List can't be concatenated with int - Error
# #l4 = l3 + 12
#
# #concatenation with list without reference
# l4 = l3 + [4]
# print(l4)
#
# #concatenation with inbuild function - but it will modify the same list
# l1.extend([4,5,6])
# print(l1)


# l1 = [1, 2, 3]
#
# #Note: multiplying number should be whole number otherwise error
# l2 = l1 * 3
# print(l2)

# l1 = [1, 2, 3]
# print(3 in l1)
#
# l2 = [[1,2], [3,4], 5]
# print(2 in l2)
# print([3,4] in l2)
#
# #Application of in operation  in for loop
# l3 = ["red", "green", "blue"]
# for item in l3:
#     print(item)


# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = [3, 2, 1]
#
# print(l1 == l2)
# print(l1 == l3)
# print(l1 != l3)

l1 = [1, 2, 3, 1]
l2 = [1, 2, 0, 4]
l3 = [1, 2, 1]

print(l1 < l2)
print(l3 < l1)
print(l3 > l2)




















