"""
Check whether a given integer is single-digit, double-digit, or multi-digit
"""

try:
    user_input = input("Enter a valid integer: ").strip()

    if user_input == "":
        print("Please enter a valid integer")
    else:
        number = abs(int(user_input))
        
        if number <= 9:
            print(f"Number {number} is single-digit")
        elif 9 < number <= 99:
            print(f"Number {number} is double-digit")
        else:
            print(f"Number {number} is multi-digit")

except Exception as e:
    print(f"Something went wrong: {e}")
