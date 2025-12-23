n = int(input("Enter the number of input : "))

for i in range(1,n+1):
    if i in [1,n]:
        print(" " * (n - i) + ((str(i) + " ") * i))
    
    else:
        print(" " * (n - i) + str(i) + "  " * (i - 1) + str(i))
    print()