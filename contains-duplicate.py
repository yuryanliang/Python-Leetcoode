题目大意：
给定一个整数数组，判断数组中是否包含重复元素。如果数组中任意一个数字出现了至少两次，你的函数应该返回true，如果每一个元素都是唯一的，返回false。

解题思路：
使用set数据结构

Python代码：
解法I：

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
