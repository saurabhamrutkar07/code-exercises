# Take a character and check if it is a letter, a digit, or neither. 


try : 
    user_input = input("Enter the input : ").strip() 

    if user_input.isdigit():
        print(f"the user input {user_input} is digit ")
    elif user_input.isalpha :
        print(f"the user input {user_input} is letter ")
    else:
        print(f"the user input {user_input} is neither leter not digit")



except Exception as e : 
    print(f"Following error occurs : {e}")