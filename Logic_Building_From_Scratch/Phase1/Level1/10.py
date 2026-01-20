"""
Take a character and check whether it's uppercase, lowercase, a digit, or a special character
"""

try:
    user_input = input("Enter a single character: ").strip()

    if len(user_input) != 1:
        print("Enter a single character")
    else:
        if user_input.isdigit():
            print(f"Character {user_input} is a digit")
        elif user_input.islower():
            print(f"Character {user_input} is lowercase")
        elif user_input.isupper():
            print(f"Character {user_input} is uppercase")
        else:
            print(f"Character {user_input} is a special character")
except Exception as e:
    print(f"Something went wrong: {e}")
