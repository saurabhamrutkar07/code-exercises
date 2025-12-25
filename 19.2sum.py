def twoSum(nums,target):
    seen = {}

    for i in range(len(nums)):
        difference = target - nums[i] 

        if difference in seen:
           return [seen[difference],i] 
        else :
            seen[nums[i]] = i


tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 5, 3, 7], 8, [0, 3]),
    ([0, 4, 3, 0], 0, [0, 3])
]

for nums, target, expected in tests:
    result = twoSum(nums, target)
    print("nums =", nums, "target =", target,
          "result =", result, "expected =", expected)
