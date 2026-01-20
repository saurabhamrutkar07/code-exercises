def removeDuplicates( nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1  # index of last unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


def main():
    # Test case 1
    nums = [1, 1, 2]
    k = removeDuplicates(nums)
    print("k =", k)
    print("nums =", nums[:k])

    # Test case 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(nums)
    print("k =", k)
    print("nums =", nums[:k])

    # Test case 3
    nums = []
    k = removeDuplicates(nums)
    print("k =", k)
    print("nums =", nums[:k])


if __name__ == '__main__':
     main()



     