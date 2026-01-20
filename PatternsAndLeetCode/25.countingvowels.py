s= 'programming'

vowels = ['a','e','i','o','u']
count = 0
for ch in s:
    if ch in vowels:
        count += 1 

print(count)


vowels_set = {'a','e','i','o','u'}

count = sum(1 for ch in s if ch in vowels_set)