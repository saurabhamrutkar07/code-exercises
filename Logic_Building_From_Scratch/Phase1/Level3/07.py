"""
Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
"""

denomination = {
    2000 : 0, 500 : 0, 100 : 0
}

try: 
    user_input = input("Enter the valid amount : ").strip()
    if user_input == "" :
        print("Please enter the valid input")
    else:
        amount = int(user_input)
        if amount // 2000 > 0 :
            denomination[2000] = amount // 2000
            amount = amount % 2000
        if amount // 500 > 0:
            denomination[500] = amount // 500
            amount = amount % 500 
        if amount // 100 > 0 :
            denomination[100] = amount // 100 
            amount = amount % 100 

        print(denomination)
        print(f"remaining amount that can not de dispencend in 2000, 500, 100 is {amount}")
        
except Exception as e :
    print(f"Something went wrong : {e}")

