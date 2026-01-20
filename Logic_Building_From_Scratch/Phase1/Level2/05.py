"""
Take the hour of the day (0-23) and print "Good Morning", "Good Afternoon",
"Good Evening", "Good Night"
"""

try:
    user_input = input("Enter the valid hour (0-23): ").strip()

    if user_input == "":
        print("Please enter a valid hour")
    else:
        time = float(user_input)
        if 0 <= time <= 23:
            if 5 <= time < 12:
                print("Good Morning")
            elif 12 <= time < 17:
                print("Good Afternoon")
            elif 17 <= time <= 21:
                print("Good Evening")
            else:
                print("Good Night")
        else:
            print("The entered time is invalid")

except Exception as e:
    print(f"Something went wrong: {e}")
