def collattz(n):
    if n % 2 == 0:
        return ( n // 2)
    else:
        return ( 3 * n + 1)

n = (int(input("Enter the integer: ")))
while True:
    n = collattz(n)
    print(n)
    if n == 1:
        break