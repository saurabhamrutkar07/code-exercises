# . Take a password string and check basic rules (length ≥ 8 and contains at least one  digit). 

try: 
    password = input("Enter the password : ")

    if any(ch.isdigit() for ch in password)  and len(password) >= 8:
        print("User enter the valid password")
    else : 
        print("User enter the invalid password")

except Exception as e : 
    print(f"Following error occurs : {e}")