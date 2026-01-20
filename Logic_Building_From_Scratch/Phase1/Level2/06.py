"""
Check voting eligibility of given age (18+)
"""


try:
    user_input = input("Enter the valid age(number) : ").strip() 

    if user_input == "":
        print("Please enter the valid age(number)")
    else:
        age = float(user_input)
        if 0 < age < 113 :
            if age > 18: 
                print("You are eligible for voting")
            else:
                print("You are not eligible for voting") 
        else:
            print(f"Age {age} is invalid")

except Exception as e:
    print(f"Something went wrong : {e}")
