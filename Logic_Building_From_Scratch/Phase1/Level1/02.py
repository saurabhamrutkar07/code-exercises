"""
Check if number is even or odd 
"""

try:
    user_input = input("Enter the input : ").strip()
    if user_input == "":
        print("Enter valid input")
    else:
        number = int(user_input)

        if number % 2 == 0:
            print("even")
        else:
            print("odd")
     
except Exception as e :
    print(f"{e}")

