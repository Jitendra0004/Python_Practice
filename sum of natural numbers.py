n = int(input("Enter the number : "))
if n < 0:
    print("Try again")
else:
    sum = 0
    while(n > 0):
        sum += n
        n -= 1
    print(sum)