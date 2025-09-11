# First Pattern:

# for i in range(5):
#
#     for j in range(5):
#         print("*", end=" ")
#
#     print("")

# Second Pattern:

# for i in range(5):
#
#     # for j in range(5):
#     #     if j <= i:
#     #         print("*", end=" ")
#
#     for j in range(i + 1):
#         print("*", end=" ")
#
#     print("")

# Second Pattern - Using one single for loop taking advantage of repeatation function of python
# for i in range(1, 6):
#     print("* " * i)


# Thrid Pattern

# for i in range(5, 0, - 1):
#
#     for j in range(i):
#         print("*", end=" ")
#
#     print("")

# Fourth Pattern

for i in range(5):

    for j in range(5):

        if j < i:
            print(" ",end="")
        else:
            print("*", end="")

    print("")
