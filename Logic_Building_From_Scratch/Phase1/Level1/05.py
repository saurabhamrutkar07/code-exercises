"""
Check oif given year is leap or not 
"""

try:
    user_input = input("Enter the input : ").strip()

    if user_input == "":
        print("Enter the valid input")
    else:
        year = int(user_input)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("Year is leap year") 
        else:
            print("Year is not leap year")
except Exception as e:
    print(f"somthing went wrong : {e}")


