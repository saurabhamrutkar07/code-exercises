s1 = 'abc'
s2 = 'pqr'

result = []

i = 0 

while i < len(s1) or i < len(s2):
    if i < len(s1):
        result.append(s1[i])
    if i < len(s2):
        result.append(s2[i])

    i += 1 

print("".join(result))


