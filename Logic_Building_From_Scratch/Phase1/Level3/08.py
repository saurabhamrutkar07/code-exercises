"""
Check if a number lies within the range [100, 999].
"""

try:
    user_input = input("Enter the valid number : ").strip()
    if user_input == "":
        print("Please enter the valid input")
    else:
        number = abs(int(user_input))
        if 99 < number < 1000:
            print(f"Number {number} lies between 100 and 999")
        else:
            print(f"Number {number} does not lie between 100 and 999") 
except Exception as e:
    print(f"Something went wrong : {e}")
