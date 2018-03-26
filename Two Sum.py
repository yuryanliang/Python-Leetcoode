题目原文
Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
You may assume that each input would have exactly one solution.

Example: 
Given nums = [2, 7, 11, 15], target = 9, 
Because nums[0] + nums[1] = 2 + 7 = 9, 
return [0, 1].

题目翻译
给定一个整数数组nums，返回数组中“和是某个给定值target”的两个数的下标。假设对于每次输入有且只有一个解。 
比如：给定nums = [2, 7, 11, 15]，target = 9，因为nums[0] + nums[1] = 2 + 7 = 9，所以返回[0, 1]。

思路方法
思路一
直观思路，暴力求解，两重循环。效率很低。。。

代码

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums) - 1):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
1
2
3
4
5
6
7
8
9
10
11
思路二
由于题目说了有且只有唯一解，可以考虑两遍扫描求解：第一遍扫描原数组，将所有的数重新存放到一个dict中，该dict以原数组中的值为键，原数组中的下标为值；第二遍扫描原数组，对于每个数nums[i]查看target-nums[i]是否在dict中，若在则可得到结果。 
当然，上面两遍扫描是不必要的，一遍即可，详见代码。

代码

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in xrange(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i
                
                # Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
