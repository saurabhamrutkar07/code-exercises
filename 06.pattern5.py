n = int(input('Enter the number input : '))
half = n // 2
for i in range(1, 2 * n + 1):
    i
    if i > n: 
        print("* " * (2 * n - i))
    else:
        print("* "  * i)