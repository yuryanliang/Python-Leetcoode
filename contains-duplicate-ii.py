题目链接
https://leetcode.com/problems/contains-duplicate-ii/

题目原文
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

题目翻译
给定一个数组，和一个整数k，判断该数组中是否存在不同下标的 i 和 j 两个元素，使得 nums[i] = nums[j]，且 i 和 j 的差不超过k。

思路方法
暴力两重循环不可取，无法AC。。。

思路一
遍历所有元素，将元素值当做键、元素下标当做值，存放在一个字典中。遍历的时候，如果发现重复元素，则比较其下标的差值是否小于k，如果小于则可直接返回True，否则更新字典中该键的值为新的下标。

代码

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = {}
        for i in xrange(len(nums)):
            if nums[i] in num_map and i - num_map[nums[i]] <= k:
                return True
            else:
                num_map[nums[i]] = i
        return False
