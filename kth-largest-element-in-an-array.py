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
Method 1: Quickselect
Please see Quickselect.

Step 1: select nums[0] as pivot
Step 2: tail means the end of window that all elements are larger than pivot
Step 3: swap pivot with nums[tail]
If tail + 1 == k: return pivot. Since (tail) elements larger than pivot, so pivot is (tail + 1)th largest
If tail + 1 < k: result is among the window excluding pivot, so cut off nums to nums[:tail](nums[tail] is pivot, kicked out)
If tail + 1 > k: result is outside of window, so cut off nums to nums[tail+1:].

Python:
 class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        tail = 0

        for i in range(1, len(nums)):
            if nums[i] > pivot:
                tail += 1
                nums[tail], nums[i] = nums[i], nums[tail]
        
        nums[tail], nums[0] = nums[0], nums[tail]
        
        if tail + 1 == k:
            return pivot
        elif tail + 1 < k:
            return self.findKthLargest(nums[tail+1:], k - tail - 1)
        else:
            return self.findKthLargest(nums[:tail], k)  #excluding pivot
Complexity:
O(n) time average
O(1) space
Method 2: Heap
Push (-value) to a heap, then pop the (-minimum value)=maximum value.

Python:
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap = []
        res = 0
        
        for i in nums:
            heapq.heappush(heap, -i)
        
        for j in range(k):
            res = -heapq.heappop(heap)
        
        return res
Complexity:
O(n) time
O(n) space

    题目描述：
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

题目大意：
从一个未经排序的数组中找出第k大的元素。注意是排序之后的第k大，而非第k个不重复的元素

测试样例如题目描述

可以假设k一定是有效的， 1 ≤ k ≤ 数组长度

解题思路：
O(n)解法：快速选择（QuickSelect）算法，参考耶鲁大学关于QuickSelect算法的介绍

O(nlogn)解法：排序

Python代码：
O(n)解法：快速选择算法

import random
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot
O(nlogn)解法：排序    
    class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]
