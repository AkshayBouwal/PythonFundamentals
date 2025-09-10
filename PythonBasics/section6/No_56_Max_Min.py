n = 5
i = 0
print("Enter the 5 Numbers: ")

maximum = float('-inf')  # - infinity
minimum = float('inf')  # + infinity

while i < n:

    num = int(input())

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    i += 1

print("Maximum value: ", maximum)
print("Minimum value: ", minimum)
