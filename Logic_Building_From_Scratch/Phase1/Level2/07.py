"""
Take two numbers and determine whether both are even or both are 
odd, or one is even and one is odd  
"""

try:
    user_input = input("Enter 2 valid numbers separated by single space : ").strip().split() 

    if len(user_input) != 2 :
        print("Please enter valid inputs separated by single space")
    else:
        num1,num2 = map(int,user_input)

        if num1 % 2 == 0 and num2 % 2 == 0 :
            print("Both numbers are even")
        elif num1 % 2 != 0 and num2 % 2 != 0:
            print("Both numbers are odd")
        elif (num1 % 2 == 0 and num2 % 2 != 0) or  (num1 % 2 != 0 and num2 % 2 == 0):
            print("One number is even and one number is odd")
except Exception as e : 
    print(f"Something went wrong : {e}")