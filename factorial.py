n = int(input("Enter the number : "))
factorial = 1
if n <=0:
    print("Invalid input")
else:
    for i in range(1,n+1):
        factorial = factorial * i
    print("The factorial of",n,"is",factorial)