s = 'programming'

vowels = {'a','e','i','o','u'}

count = sum(1 for ch in s if ch not in vowels)

print(count)
