def isprime(n):
    Flag = False
    if(n % 2 == 0):
        return False
    else:
        for i in range(2,n):
            if (n % i == 0):
                Flag = True
                break
        return True
    
def countprimes(list_of_numbers):
    count =0
    for num in list_of_numbers:
           count = count+1
    return(count)  