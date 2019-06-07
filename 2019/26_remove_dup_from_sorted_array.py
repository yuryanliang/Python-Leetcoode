class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        last = 0
        i = 1
        while i < len(nums):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
            i += 1
        return last + 1
