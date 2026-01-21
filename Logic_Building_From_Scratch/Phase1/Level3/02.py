"""
Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.
"""

try:
    user_input = input("Enter a 3-digit number: ").strip()

    if len(user_input) != 3:
        print("Enter a valid 3-digit number")
    else:
        number = abs(int(user_input))
        if 99 < number < 1000:
            a = number // 100 
            b = (number // 10) % 10
            c = number % 10

            if b > a and b > c:
                print(f"Middle digit {b} is the largest among all digits")
            elif b < a and b < c:
                print(f"Middle digit {b} is the smallest among all digits")
            else:
                print(f"Middle digit {b} is neither the smallest nor the largest") 
        else:
            print("The number is invalid. Please enter a valid 3-digit number") 

except Exception as e:
    print(f"Something went wrong: {e}")
