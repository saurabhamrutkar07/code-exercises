"""
Check if number is divisible by 5 
"""


try:
    user_input = input("Enter the number : ").strip()
    if user_input == "":
        print("Enter the valid input ")
    else: 
        number = int(user_input)
        if number % 5 == 0:
            print("number is divisible by 5")
        else:
            print("number is not divisible by 5")
except Exception as e:
    print(f"{e}")
