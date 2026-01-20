"""
Take three number and print the largest 
"""


try:
    user_input = input("Enter the three number separated by exactly single space : ").strip().split()

    if len(user_input) != 3 :
        print("enter exctly 3 numbers separated by space ")
    else:
        a = float(user_input[0])
        b = float(user_input[1])
        c = float(user_input[2])

        if a > b and a > c :
            print(f"the largest number is {a}")
        elif b > a and b > c:
            print(f"the largest number is {b}")
        elif c > a and c > b: 
            print(f"the largest number is {c}")
        else:
            print("all numbers are same ")

except Exception as e:
    print(f"somthing went wrong : {e}")