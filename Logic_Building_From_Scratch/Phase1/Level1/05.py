"""
Check if given year is leap or not 
"""

try:
    user_input = input("Enter a Year : ").strip()

    if user_input == "":
        print("Enter the valid input")
    else:
        year = int(user_input)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("Year is a leap year") 
        else:
            print("Year is not a leap year")
except Exception as e:
    print(f"something went wrong : {e}")


