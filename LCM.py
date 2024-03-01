
def LCM(x,y):
    if x > y :
        greater = x
    else:
        greater = y
    
    while(True):
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm
n1 = int(input("Enter the  number: "))
n2 = int(input("Enter the number : "))

print("LCm of",n1,"and",n2,"is: ",LCM(n1,n2))