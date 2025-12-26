def isValid(s: str) -> bool:
    stack = []
    mapping = {"}": "{","]":"[",")":"("}
    for ch in s : 
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

tests = [
    ("()", True),
    ("()[]{}", True),
    ("{[()]}", True),
    ("", True),
    ("((([{}])))", True),
    ("(]", False),
    ("([)]", False),
    ("((()", False),
    (")(", False),
    ("{[}", False)
]

for s, expected in tests:
    result = isValid(s)
    print(f"s = '{s}' → result = {result}, expected = {expected}")


stack = []

my_dict = {

    '}' : '{',
    ')' : '(',
    ']' : '['    
    
    }

