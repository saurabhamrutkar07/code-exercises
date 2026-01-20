"""
Take a number and print wherather its positive, negative or zero 

"""

try : 
    user_input = input("Enter the the number : ").strip()

    if user_input == "":
        print("Enter valid integer")
    
    else:
        number = float(user_input)
        if number > 0 :
            print("positive")
        elif number < 0 :
            print("negative")
        else:
            print("zero")

except ValueError as e :
    print(f"{e}")