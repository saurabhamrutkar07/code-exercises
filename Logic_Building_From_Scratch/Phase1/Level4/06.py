# Take two numbers and check if both are positive and their sum is less than 100.  

try : 
    numbers = list(map(int,input("Enter the two numbers separated by comma, : ").split(",")))
    
    if numbers[0]> 0 and numbers[1] > 0 and (numbers[0]+ numbers[1] < 100):
        print(f"{numbers[0]} and {numbers[1]} are positive and their sum is less than 100 ")

except Exception as e : 
    print(f"Following error occurs : {e}")