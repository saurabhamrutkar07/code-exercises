# Take a single digit (0–9) and print its word form (“Zero” to “Nine”). 


try:
    nums_dict = {0:"zero",1:"one",2:"two",3:"three",4:'four',5:"five",6:"six",7:'seven',8:'eight',9:'nine'}
    user_input = int(input("Enter the number from 0 to 9 : "))

    if 0 <= user_input <= 9:
        print(f"{user_input} is {nums_dict[user_input]}")


except Exception as e : 
    print(f"Following errors : occurs : {e}" )