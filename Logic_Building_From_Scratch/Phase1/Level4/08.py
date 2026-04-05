# Take a weekday number (1–7) and determine if it is a weekday or weekend.


try: 
    user_input = int(input("Enter the numbewr of day from 0 to 7 I will decide its weekday or weekend : "))

    if 1 <= user_input <= 5 : 
        print('Its a week day')
    elif user_input in [6,7]:
        print("Its a weekend")
    else:
        print("Invalid day enter valid week day") 

except Exception as e : 
    print(f"following error occurs : {e}")