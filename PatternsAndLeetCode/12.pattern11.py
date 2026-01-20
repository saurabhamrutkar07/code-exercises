n = int(input('Enter the number of input : '))

for i in range(1,n+1):
    if i in [1,2,n]:
        print('* ' * i)
    else: 
        print("* " + "  " * (i - 2) + "* " )
    #print("* " * i)