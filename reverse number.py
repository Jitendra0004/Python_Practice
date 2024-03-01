n = int(input("Enter the number to reverse : "))
reverse = 0
while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit 
    n //= 10
print("Reversed Number : ",reverse)