"""
Take three numbers and print the largest
"""

try:
    user_input = input("Enter the three numbers separated by exactly a single space: ").strip().split()

    if len(user_input) != 3:
        print("Enter exactly 3 numbers separated by space.")
    else:
        a = float(user_input[0])
        b = float(user_input[1])
        c = float(user_input[2])

        if a > b and a > c:
            print(f"The largest number is {a}")
        elif b > a and b > c:
            print(f"The largest number is {b}")
        elif c > a and c > b: 
            print(f"The largest number is {c}")
        else:
            print("All numbers are the same.")

except Exception as e:
    print(f"Something went wrong: {e}")
