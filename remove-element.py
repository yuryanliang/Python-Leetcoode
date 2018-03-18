# Time:  O(n)
# Space: O(1)
#
# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        last = len(nums) - 1
        
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last-=1
            else:
                i+=1
        return last + 1
