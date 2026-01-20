"""
Take a alphabet character and check if it lies between 'a' and 'm'
or 'n' and 'z'
"""

try:
    character = input("Enter a single character : ").strip()

    if len(character) != 1 : 
        print("Only enter the single character ")
    else:
        if ord('a') <= ord(character.lower()) <= ord('m'):
            print(f'character {character} is between a and m')
        elif  ord('n') <= ord(character.lower()) <= ord('z'):
            print(f'character {character} is between n and z') 
        else:
            print(f"character {character} is not between a to m and n to z")
except Exception as e :
    print(f"Something went wrong : {e}")
