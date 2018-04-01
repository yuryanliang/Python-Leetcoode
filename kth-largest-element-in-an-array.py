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
