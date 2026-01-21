"""
Take a 3 digit number and check if all digits are distinct
"""


try:
    user_input = input("Enter the 3 digit number : ").strip()

    if len(user_input) != 3:
        print("Enter the valid input")
    else:
        number = int(user_input)
        number = abs(number)
        if 99 < number < 1000:
            a = number // 100 
            b = int((number // 10) % 10)
            c = int(number % 10) 
            if a != b != c  or (a !=b and b != c and c != a): 
                print("All three digits are distinct")
            else:
                print("All three digits are not distinct") 
        else:
            print("Please enter valid 3 digit number")

except Exception as e :
    print(f"Something went wrong : {e}")


