"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""

#sliding window
class Solution:
    def minSubArrayLen(self, s, nums) :
        start = 0
        sum = 0
        import sys
        min_size = sys.maxsize
        for i in range(len(nums)):
            sum +=nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start +=1
        return min_size if min_size != sys.maxsize else 0

    def min(self,s, nums):
        start = 0
        sum =0

        import sys
        min_size = sys.maxsize

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start +=1
        return min_size if min_size != sys.maxsize else 0
