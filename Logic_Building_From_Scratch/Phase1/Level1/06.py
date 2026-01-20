"""
Take 2 numbers and print the larger one
"""

try:
    two_numbers = input("Enter the two numbers : ").strip().split()
    
    if len(two_numbers) != 2 :
        print("Please enter exactly two numbers separated by space")
    
    else:
        a = int(two_numbers[0])
        b = int(two_numbers[1])

        if a > b : 
            print(f"Greater number is {a}")
        elif b > a:
            print(f"Greater number is {b}")
        else:
            print("both the numbers are same")
    
except Exception as e:
    print(f"somthing went wrong : {e}")