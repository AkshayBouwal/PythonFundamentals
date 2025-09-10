# num = 0
#
# while True:
#
#     if num >= 10:
#         break
#
#     num += 1
#     print(num)

#use of continue keyword

num = 0

while num < 10:

    num += 1

    if num % 2 != 0:
        continue

    print(num)



