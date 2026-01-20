"""
Take a number and print whether it is positive, negative or zero
"""

try: 
    user_input = input("Enter the number: ").strip()

    if user_input == "":
        print("Enter a valid number")
    else:
        number = float(user_input)
        if number > 0:
            print("positive")
        elif number < 0:
            print("negative")
        else:
            print("zero")

except ValueError as e:
    print(f"{e}")
