l1 = [5, 6, 7, 8, 9]

print("Using for each loop :" ,end= " ")
for x in l1:
    print(x, end=" ")
print()

print("Using For Loop with range:" ,end= " ")
for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

print("Using While Loop:" ,end= " ")
i = 0
while i < len(l1):
    print(l1[i], end=" ")
    i = i + 1
