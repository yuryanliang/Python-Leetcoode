# Time:  O(n)
# Space: O(1)
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
import collections


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1
        
        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1
        
        return nums[idx]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
    
#思路一
#（HashTable）遍历数组，用一个字典记录所有出现过的元素及其个数。由于题目说明多数元素一定存在，故当找到某个元素出现次数大于 ⌊ n/2 ⌋ 时即可停止。

#代码一

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = {}
        for i in nums:
            digits[i] = digits.get(i, 0) + 1
            if digits[i] > len(nums)/2:
                return i
#类似的，也可以考虑用集合这一数据结构。先找出数组中的所有不同的数，相当于“取原数组的集合”的操作，然后判断该集合中的每个数在数组中出现次数是否过半 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        for i in nums_set:
            if nums.count(i) > len(nums)/2:
                return i
                
                
 #               思路二
#（Sort）先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素。
   class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]            
