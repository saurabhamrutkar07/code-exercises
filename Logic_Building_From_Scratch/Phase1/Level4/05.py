# Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

try:
    income = float(input("Enter the income in digits : "))
    age = float(input("Enter the age (e.g., 500000 for 5 Lakh) : ")) 

    if age > 18 and income > 500000:
        print("You are eligible for tax")
    else:
        print("You are not eligible for tax")


except Exception as e :
    print(f"Following error occurs : {e}")