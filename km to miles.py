n = int(input("Enter the Kilometeres: "))
if n<=0:
    print("Input is not valid")
else:
    miles = n * 0.6213711922
    print(n,"kilometers is equal to ",(miles),"miles")