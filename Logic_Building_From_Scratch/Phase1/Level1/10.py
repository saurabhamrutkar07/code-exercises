"""
Take a character and check wheather its uppercase, lowercase, a digit or a special character 
"""

try:
    user_input = input("Enter a single character : ").strip()

    if len(user_input) != 1:
        print("Enter the single character")
    else:
        if user_input.isdigit() :
            print(f"character {user_input} is digit")
        elif user_input.islower():
            print(f"character {user_input} is lower case")
        elif user_input.isupper():
            print(f"character {user_input} is upper case")
        else:
            print(f"character {user_input} is special character")
except Exception as e :
    print(f"somthing went wrong : {e}")
