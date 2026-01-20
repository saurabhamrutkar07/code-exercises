"""
Take a temprature value and print Cold, Warm and Hot using range condition
"""


try:
    user_input = input("Enter the temprature : ").strip() 

    if user_input == "":
        print("Enter the valid input")
    else:
        temprature = float(user_input)

        if temprature < 15 :
            print("Cold")
        elif 16 <= temprature <= 30 :
            print("Warm")
        elif temprature > 30:
            print("Hot") 

except Exception as e:
    print(f"somthing went wrong : {e}")