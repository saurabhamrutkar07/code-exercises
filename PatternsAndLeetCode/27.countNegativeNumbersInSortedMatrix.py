from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        r, c = 0, cols - 1   # start at top-right
        count = 0

        while r < rows and c >= 0:
            if grid[r][c] < 0:  # negative found
                count += rows - r   # count all negatives in this column
                c -= 1              # move left
            else:  # positive or zero
                r += 1              # move down

        return count

# -------------------------------
# TEST CASE
# -------------------------------

grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]

solution = Solution()
result = solution.countNegatives(grid)
print("Number of negative numbers:", result)  # Expected output: 8
