"""
Check wheather the number is perfect square or not without using square root function
"""


try:
    user_input = input("Enter the valid integer : ").strip()

    if user_input == "":
        print("Please enter the valid input")
    else: 
        number = int(user_input)

        if number < 0 :
            print(f"{number} can not be perfect square")
        else:
            for i in range(1, number//2):
                if i * i == number:
                    print(f"{number} is a perfect square")
                    break
            print(f"{number} is not a perfect square")

except Exception as e : 
    print(f"Something went wrong : {e}")


"""
Second approach 
"""

is_found = False

try: 
    user_input = input("Enter the valid integer : ").strip()
    
    if user_input == "":
        print("Please enter the valid input")
    else:
        number = int(user_input)

        if number < 0 : 
            print(f"{number} is not a perfect square ")
        elif number in [0,1]:
            print(f"{number} is perfect square")
        else:
            low = 2 
            high = number - 1 
            # mid = low + high // 2 

            while low <= high:
                mid = (low + high) // 2
                square = mid * mid 

                if square == number:
                    is_found = True
                    break
                elif square < number:
                    low = low + 1 
                else:
                    high = mid - 1
            
            if is_found : 
                print(f"{number} is a perfect square")
            else:
                print(f"{number} is not a perfect square")

            

except Exception as e : 
    print(f"Something went wrong : {e}")