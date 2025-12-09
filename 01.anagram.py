s1 = input('Enter the first string : ').strip().lower()
s2 = input('Enter the second string : ').strip().lower()

if len(s1) != len(s2):
    print("No")

l = list(s2)

for ch in s1:
    if ch in l:
        l.remove(ch)
    else:
        print("No")
        break

else:
    print("Yes")