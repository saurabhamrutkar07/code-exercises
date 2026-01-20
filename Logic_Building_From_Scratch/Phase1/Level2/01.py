"""
Take three sides and check if they form a valid triangle. 
"""

try:
    user_input = input("Enter the sides of triangle: ").strip().split() 
    if len(user_input) != 3:
        print("Please enter exactly three numbers separated by spaces.")

    side1, side2, side3 = map(float, user_input)

    if side1 > 0 and side2 > 0 and side3 > 0 and (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2: 
        print("The triangle is a valid triangle")
    else:
        print("The triangle is invalid")
except Exception as e:
    print(f"Something went wrong: {e}")
