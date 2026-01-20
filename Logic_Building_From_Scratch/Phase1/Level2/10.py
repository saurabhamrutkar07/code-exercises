"""
Take a month number (1 to 12 ) and print the number of days in that month ignoring the leap year 
"""
moths = { 1 : "January", 2 : "February", 3: "March", 4: "April", 5: "May", 6:"June",
         7:"July", 8:"August", 9: "September", 10: "Octomber", 11: "November", 12: "Dececber"
         }

try: 
    user_input  = input("Enter the valid month between 1 and 12 : ").strip()

    if user_input == "":
        print("Please enter the valid input")
    
    else:
        month = int(user_input)

        if 1 <= month <= 12 :
            if month in [1,3,5,7,8,10,12]:
                print(f"{moths[month]} has 31 days")
            elif month in [4,6,9,11]:
                print(f"{moths[month]} has 30 days")
            else : 
                print(f"{moths[month]} has 28 days")
        else:
            print("Invalid month")

except Exception as e :
    print(f"Something went wrong : {e}")
    
