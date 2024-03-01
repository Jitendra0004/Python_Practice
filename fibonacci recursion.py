def recursion_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursion_fibonacci(n-1)+recursion_fibonacci(n-2)
    
    
n = int(input())
if n <= 0:
    print("Input must be a positive integer")
else:
    print("fibonacci sequence: ")
    for i in range(n):
        print(recursion_fibonacci(i))
    