"""
Check if one of two numbers are multiple of other
"""

try:
    user_input = input("Enter two space-separated numbers: ").strip()

    if user_input == "":
        print("Please enter two space-separated numbers.")
    else:
        num1, num2 = map(int, user_input)

        if num2 != 0 and num1 % num2 == 0:
            print(f"{num1} is a multiple of {num2}")
        elif num1 != 0 and num2 % num1 == 0:
            print(f"{num2} is a multiple of {num1}")
        else:
            print("Neither number is a multiple of the other.")

except Exception as e:
    print(f"Something went wrong: {e}")
