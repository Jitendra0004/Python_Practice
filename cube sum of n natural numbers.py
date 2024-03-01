def cube_sum_of_natural_numbers(n):
    if n < 0:
        return(0)
    else:
        total = sum([i**3 for i in range(1, n+1)])
        return total
    
n = int(input(" Enter the number : "))
result = cube_sum_of_natural_numbers(n)
print(f"The cube is : ",result)