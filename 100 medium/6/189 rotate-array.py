"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        if k == 0:
            return
        first= nums[-k:]
        print(first)
        second = nums[:-k]
        print(second)
        nums[:k]= first
        print(nums)
        nums[k:]=second
        print(nums)

class Solution1:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            previous = nums[-1] #initiate a first previous
            for i in range(len(nums)):

                previous,nums[i]= nums[i], previous
        print(nums)

class Solution4:
    def rotate(self, nums, k) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
if __name__ == '__main__':
    nums =[1,2,3,4,5,6,7]
    k = 3
    # nums =[1]
    # k = 0
    Solution1().rotate(nums, k)
    print(nums)