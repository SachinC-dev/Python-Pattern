n = int(input("Enter number: "))
for i in range(1, n+1):     #about row
    print(" "*(n-i), end="")
    for j in range(1, i+1): #about column
        print(j, end='')
    for e in range(i-1, 0, -1): #about column
        print(e, end="")
    print()