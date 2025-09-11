# num = int(input('Enter a Natural Number: '))
#
# sum = 0
#
# for i in range(1,num+1):
#     sum += i
#
# print(f"Sum of first {num} is: ", sum)

num = int(input('Enter a number: '))
fact = 1
for i in range(num, 0, -1):
    print(f"{i} * {fact}")
    fact *= i
    print(fact)

print(f"The factorial of {num} is: {fact}")
