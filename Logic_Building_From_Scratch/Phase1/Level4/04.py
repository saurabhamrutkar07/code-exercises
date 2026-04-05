# Take 24-hour time (hours and minutes) and print whether it is AM or PM.


try :
    user_input = input("Enter the time in such format 10:10: ")
    hour = int(user_input.split(":")[0])
    minutes = int(user_input.split(":")[1])
    if not(0 <= hour <= 23):
        print("Invalid hours")
    elif not (0 <= minutes <= 59):
        print("Invalid Minutes")
    else:
        display_hour = hour % 12
        if display_hour == 0:
            display_hour = 12 
        period = "AM" if hour < 12 else "PM"
        
        print(f"{display_hour}:{minutes}{period}")

except Exception as e :
    print("Follwing error occurs : {e}")