# Take electricity units consumed and calculate the bill as per slabs (using if-else).


try : 
    cost = 0
    units = float(input("Enter the number of units : ")) 

    if 0 <= units <= 100 :
        cost = units * 5 
    elif 101 <= units <= 200 :
        cost = (units - 100) * 7 + (100 * 5) 
    elif 201 <= units <= 500 :
        cost = (units - 200) * 10 + (100 * 7) + (100 * 5)
    else:
        cost = (units - 500 )* 15 + (300 * 10) + (100 * 7) + (100 * 5)
    
    print(f"Total electricit bill is : {cost} for units {units}")

except Exception as e :
    print(f"Following error occurs : {e}")