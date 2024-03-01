n = int(input("Enter the Table number you Want: "))
if(n<=0):
    print("invalid input, Try again")
else:
    for i in range(1,12):
        print( n ,"x",i,"=",n*i)