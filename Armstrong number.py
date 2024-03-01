n = int(input("Enter the Number: "))
sum = 0
temp = n
while temp > 0:
    digits = temp % 10
    sum += digits ** 3
    temp //= 10
if n == sum:
    print(n,"is a armstrong number")
else:
    print(n,"is not an armstrong number")
