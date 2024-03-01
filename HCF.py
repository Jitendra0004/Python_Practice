def hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

n1= int(input("Enter the number: "))
n2 =int(input("enter the number : "))
print ("The H.C.F of", n1,"and", n2 ,"is : ",hcf(n1,n2))