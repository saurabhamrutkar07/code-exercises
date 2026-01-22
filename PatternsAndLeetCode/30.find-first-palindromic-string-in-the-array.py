from typing import List
# Approch 1 
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word.lower() == word[::-1].lower():
                return word 
                break 


        return "" 
        


# Approch 2 

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word)->bool:
                left,right = 0,len(word) - 1
                while left < right :                
                    if word[left] != word[right]:
                        return False
                    left += 1
                    right -= 1

                return True
        for word in words:
            if is_palindrome(word):
                return word
        
        return ""
    

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ["abc","car","ada","racecar","cool"],
        ["racecar","level","noon"],
        ["hello","world"],
        ["a","b","c"],
        ["Abcba","hello"]
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"Test case {i}: {sol.firstPalindrome(case)}")
