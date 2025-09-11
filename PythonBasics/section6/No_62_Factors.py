# num = int(input("Enter a number whose factors you want to find: "))
#
# for i in range(1, num + 1):
#
#     if num % i == 0:
#         print(i)


# num = int(input("Enter a number to check for Prime or Not: "))
#
# count = 0
#
# for i in range(1, num + 1):
#
#     if num % i == 0:
#         count += 1
#
# if count == 2:
#     print(f"{num } is a prime number")
# else:
#     print(f"{num} is not a prime number")
#
#


num = int(input("Enter a number to check for Prime or Not: "))

count = 0

for i in range(2, num + 1 // 2):

    if num % i == 0:
        count += 1

if count == 0:
    print(f"{num } is a prime number")
else:
    print(f"{num} is not a prime number")


#2147483647 - Prime takes almost 5 mins to check