"""
Take a 4-digit number and check if the first and last digits are equal.
"""

try:
    user_input = input("Enter a 4-digit number: ").strip()
    
    if len(user_input) != 4:
        print("Please enter a valid number")
    else:
        number = abs(int(user_input))
        
        if 999 < number < 10000:
            a = number // 1000
            b = number % 10
            
            if a == b:
                print(f"First digit {a} and last digit {b} are the same")
            else:
                print(f"First digit {a} and last digit {b} are not the same")
        else:
            print(f"The entered number {number} is invalid")

except Exception as e:
    print(f"Something went wrong: {e}")
