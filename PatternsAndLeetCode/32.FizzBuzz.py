from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0 :
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

        


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        1,3,5,15,30,0
    ]

    for i, case in enumerate(test_cases,1):
        print(f"Test case {i}: {sol.fizzBuzz(case)}")




