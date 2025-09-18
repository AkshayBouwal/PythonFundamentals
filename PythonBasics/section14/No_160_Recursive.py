def recursion(n):

    if n  > 0:
        print(n, end=' ')
        recursion(n - 1)

recursion(5)
print()

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))