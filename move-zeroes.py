# Time:  O(n)
# Space: O(1)

# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order 
# of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after 
# calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
'''解题思路：
题目可以在O(n)时间复杂度内求解

算法步骤：

使用两个"指针"x和y，初始令y = 0

利用x遍历数组nums：

若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

算法简析：

y指针指向首个0元素可能存在的位置

遍历过程中，算法确保[y, x)范围内的元素均为0'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
