"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lookup ={}
        for n in nums:
            if n in lookup:
                lookup[n]+=1
            else:
                lookup[n] = 1

        s = sorted(lookup.values())
        1==1


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    Solution().topKFrequent(nums, k)

