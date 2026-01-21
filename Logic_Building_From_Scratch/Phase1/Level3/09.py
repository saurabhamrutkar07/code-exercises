"""
Take two angles of a triangle and compute the third angle.
"""

try: 
    user_input = input("Enter the two valid angles less than 90 separated by a single space: ").strip().split() 

    if len(user_input) != 2:
        print("Enter the two valid angles separated by a single space")
    else:
        angle1, angle2 = map(float, user_input)
        if angle1 + angle2 < 180: 
            angle3 = 180 - (angle1 + angle2)
            print(f"Third angle is {angle3}") 
        else: 
            print("You have entered invalid angles. the triangle is invalid")
except Exception as e: 
    print(f"Something went wrong: {e}")


