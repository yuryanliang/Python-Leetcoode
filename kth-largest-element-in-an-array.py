# Time:  O(n) ~ O(n^2)
# Space: O(1)

from random import randint

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = self.PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
        
    def PartitionAroundPivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in xrange(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1
            
        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx
    
    
# Time:  O(n) ~ O(n^2)
# Space: O(1)

class Solution(object):
    def quickSelect(self, nums, start, end, k):
        if start >= end:
            return nums[start]
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        
        while(left <= right):
            while(left <= right and nums[left] > pivot):
                left += 1
            while(left <= right and nums[right] < pivot):
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if (start + k - 1) <= right:
            return self.quickSelect(nums, start, right, k)
        if (start + k - 1) >= left:
            return self.quickSelect(nums, left, end, k-(left-start))
                
        return nums[right+1]
            
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return self.quickSelect(nums, 0, len(nums)-1, k)
