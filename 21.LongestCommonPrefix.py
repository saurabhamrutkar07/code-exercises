# my_list = ["flower","flow","flight"]

# my_list.sort()
# print(my_list)

# first = my_list[0]
# last = my_list[-1]

# print(first)
# print(last)

# if not my_list:
#     print("")
# i = 0 



# while i <len(first) and i < len(last) and first[i] == last[i]:
#     i += 1 

# print(first[:i])


def longest_common_substring(my_list):
    
    if not my_list:
        return ""
    
    my_list.sort()
    
    first = my_list[0]
    last = my_list[-1]

    i = 0 

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1 

    return first[:i]
test_cases = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["test", "test", "test"],
    ["alone"],
    [],
    ["", "flow", "flower"],
    ["Flower", "flow", "flight"],
    ["a", "ab", "abc"],
    ["prefix", "pre"],
    ["xa", "xb", "xc"]
]


def main():
    # Example input

    for i in test_cases:
        my_list = i
        result = longest_common_substring(my_list)
        print("Longest Common Prefix:", result)

    


if __name__ == "__main__":
    main()
    

