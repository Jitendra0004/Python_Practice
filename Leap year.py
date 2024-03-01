n = int(input("Enter the year : "))
if (n % 4 == 0) :
    print(n,"is a Leap year")
elif (n % 400 == 0) and (n % 100 == 0):
    print(n,"is a leap year")
else:
    print("not an leap year")