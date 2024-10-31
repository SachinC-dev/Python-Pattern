n = int(input("Enter number: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for k in range(i):
        print(i-k, end="")
    for e in range(2, i+1):
        print(e, end="")
    print()