"""
If the sides form the valid triangle, determine whether it is 
equilateral, isosceles or scalene 
"""

try:
    user_input = input("Enter the three sides of triangle using single space separated : ").strip().split() 

    if len(user_input) != 3:
        print("Enter the three space separated numbers")
    
    else :
    
        side1,side2,side3 = map(float,user_input)
        if side1 > 0 and side2 > 0 and side3 > 0 and (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2: 
            if side1 == side2 == side3 :
                print("Triangle is Equilateral triangle")
            elif side1 == side2 or side2 == side3 or side3 == side1 : 
                print("Triangle is Isosceles triangle")
            else:
                print("Triangle is Scalene triangle")
        else:
            print("Triangle is invalid triangle") 
except Exception as e : 
    print(f"Something went wrong : {e}")
