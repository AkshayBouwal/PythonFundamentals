l1 = [num for num in range(1,10)]
print(l1)

l1 = [num**2 for num in range(1,10)]
print(l1)

l1 = [num  for num in "Python" ]
print(l1)

l1 = [num.lower()  for num in "PyThOn" ]
print(l1)

l1 = [num  for num in "123456" ]
print(l1)

l1 = [int(num)  for num in "123456" ]
print(l1)

l1 = [num for num in "gdfja$@$#2hka@$#" if num.isalpha()]
print(l1)
