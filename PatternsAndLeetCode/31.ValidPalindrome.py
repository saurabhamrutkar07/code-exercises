class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left,right = 0,len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1 
            while  left < right and not s[right].isalnum():
                right -= 1 
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1 
             
        return True


        
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "a",
        ".,,"
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"Test case {i}: {sol.isPalindrome(case)}")
