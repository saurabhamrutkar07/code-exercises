"""
Take a temperature value and print Cold, Warm, and Hot using range condition
"""

try:
    user_input = input("Enter the temperature: ").strip() 

    if user_input == "":
        print("Enter a valid input")
    else:
        temperature = float(user_input)

        if temperature < 15:
            print("Cold")
        elif 16 <= temperature <= 30:
            print("Warm")
        elif temperature > 30:
            print("Hot") 

except Exception as e:
    print(f"Something went wrong: {e}")
