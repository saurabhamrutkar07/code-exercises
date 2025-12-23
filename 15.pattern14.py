n = int(input("Enter the number of input : "))

for i in range(1,2*n + 1):
    if i > n:
        if i != 2*n :
            print(" " * (i - n) + "* " + "  " * (2 * n - i - 1) + "* ")
        else:
            print(" " * (i - n) + "* ")
    else:
        if i in [1,2]:
            print(" " * (n - i) + "* " * i )
        else:
            print(" " * (n - i) + "*"  +  "  "  * (i - 2)  + " *")