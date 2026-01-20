"""
Take a character and check if it's vowel or consonant
"""

try:
    ch = input("Enter the single character : ").strip()

    if len(ch) != 1:
        print("Enter the single character")
    else:
        if ch.lower() in "aeiou":
            print(f"character {ch} is vowel")
        elif ch.lower() in "bcdfghjklmnpqrstvwxyz":
            print(f"character {ch} is consonant")
        else:
            print(f"character {ch} is invalid")

except Exception as e :
    print("something went wrong : {e}")