"""
Take a character and check if it's a vowel or consonant
"""

try:
    ch = input("Enter a single character: ").strip()

    if len(ch) != 1:
        print("Enter a single character")
    else:
        if ch.lower() in "aeiou":
            print(f"Character {ch} is a vowel")
        elif ch.lower() in "bcdfghjklmnpqrstvwxyz":
            print(f"Character {ch} is a consonant")
        else:
            print(f"Character {ch} is invalid")

except Exception as e:
    print(f"Something went wrong: {e}")
