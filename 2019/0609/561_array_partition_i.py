def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])