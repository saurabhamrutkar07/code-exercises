"""
Take marks 0-100 and print the corresponding grades (A/B/C/D/E/F)
"""
try:
    user_input = input("Enter the marks (0-100): ").strip() 

    if user_input == "":
        print("Please enter a valid number.")
    else:
        marks = float(user_input)

        if 100 >= marks >= 91:
            print("Grade A")
        elif 90 >= marks >= 81: 
            print("Grade B")
        elif 80 >= marks >= 71:
            print("Grade C")
        elif 70 >= marks >= 61:
            print("Grade D")
        elif 60 >= marks >= 51:
            print("Grade E")
        elif 50 >= marks >= 0:
            print("Grade F")
        else:
            print("Invalid marks.")

except Exception as e:
    print(f"Something went wrong: {e}")
