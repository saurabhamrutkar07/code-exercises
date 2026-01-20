"""
Check if number is divisible by 3 and 5 
"""


try :
    user_input = input("Enter the input : ").strip()
    if user_input == "":
        print("Enter the valid input")
    else:
        number = int(user_input)
        if number % 3 == 0 and number % 5 == 0:
            print("number is divisible by 3 and 5")
        else:
            print("number is not divisible by 3 and 5") 
except Exception as e :
    print(f"somthing went wrong : {e}")
