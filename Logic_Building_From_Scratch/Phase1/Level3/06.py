"""
Take coordinates (x, y) and determine which quadrant the point lies in.
"""

try: 
    user_input = input("Enter the two numbers separated by a single space: ").strip().split()

    if len(user_input) != 2: 
        print("Please enter exactly 2 numbers")
    else:
        x, y = map(float, user_input)

        if x == 0 and y == 0:
            print(f"Coordinates ({x}, {y}) are at the origin")
        elif x == 0:
            print(f"Coordinates ({x}, {y}) are on the Y-axis")
        elif y == 0: 
            print(f"Coordinates ({x}, {y}) are on the X-axis")
        elif x > 0 and y > 0: 
            print(f"Coordinates ({x}, {y}) are in the first quadrant")
        elif x < 0 and y > 0:
            print(f"Coordinates ({x}, {y}) are in the second quadrant")
        elif x < 0 and y < 0: 
            print(f"Coordinates ({x}, {y}) are in the third quadrant")
        elif x > 0 and y < 0: 
            print(f"Coordinates ({x}, {y}) are in the fourth quadrant")   

except Exception as e: 
    print(f"Something went wrong: {e}")

