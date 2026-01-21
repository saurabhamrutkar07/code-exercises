"""
Check if a number is a multiple of 7 or ends with 7.

"""

try: 
    user_input = input("Enter the valid number : ").strip()
    
    if user_input == "":
        print("Please enter the valid number ")
    else:
        number = abs(int(user_input))

        if number % 7 == 0:
            print(f"number {number} is divisible by 7")
        elif int(number % 10) == 7 :
            print(f"number {number} is ends with 7") 
        else: 
            print(f"number {number} is nor divisible by 7 neither ends with 7")
except Exception as e : 
    print(f"Something wnnt wrong : {e}")


