num = int(input("Enter the nth term of Fibonacci series: "))

first = 0
second = 1

for i in range(0, num):
    fib = first + second
    first = second
    second = fib

print(first)
