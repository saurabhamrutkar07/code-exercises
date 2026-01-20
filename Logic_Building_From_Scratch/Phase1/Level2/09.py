"""
Take a day number (1-7) and print the corresponding day name 
"""


days = {
    1 : "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6:"Saturday", 7: "Monday"
}

try:
    user_input = input("Enter the number between range 1 to 7 : ").strip()

    if user_input == "":
        print("Please enter the  valid number ")
    else:
        number = int(user_input)
        if 1 <= number <= 7:
            if number in days:
                print(f"number {number} is {days[number]}")
            else: 
                print(f"number {number} is invalid day. Please enter the correct number")
        else:
            print("Enter the valid number")
        

except Exception as e : 
    print(f"Something went wrong : {e}")

