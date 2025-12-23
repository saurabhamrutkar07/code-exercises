n = int(input("Enter the number of input : "))

for i in range(1,n+1):
    if i in [1,2,n]:
        print(" " * (n - i) +"* " * i)
    else:
        print(" " * (n - i)+ "* " + "  " * (i - 2) + "* ")