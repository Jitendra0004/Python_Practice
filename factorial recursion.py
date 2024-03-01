def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n-1)
    
n = int(input())
factorial = recursion_factorial(n)
print(factorial)