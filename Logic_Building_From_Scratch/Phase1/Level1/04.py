"""
Check if number is divisible by 3 and 5 
"""


try :
    user_input = input("Enter the number : ").strip()
    if user_input == "":
        print("Enter the valid number")
    else:
        number = int(user_input)
        if number % 3 == 0 and number % 5 == 0:
            print("Number is divisible by 3 and 5")
        else:
            print("Number is not divisible by 3 and 5") 
except Exception as e :
    print(f"something went wrong : {e}")
