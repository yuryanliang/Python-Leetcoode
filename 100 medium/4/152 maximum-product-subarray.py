"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


"""
local max, local min 需要同时在一行计算
"""
class Solution:
    def maxProduct(self, nums):
        import sys
        local_min, local_max, global_max = 1, 1, -sys.maxsize

        for n in nums:
            local_min,local_max = min(n, local_max * n, local_min * n), max(n, local_max * n, local_min * n)
            global_max = max(local_max, global_max)
        return global_max

    def max(self, nums):
        import sys
        local_min, local_max, global_max = 1, 1, -sys.maxsize

        for n in nums:
            local_min, local_max = min(n, local_min * n, local_max * n), max(n, local_min * n, local_max * n)
            global_max = max(global_max, local_max)
        return global_max

class Sol:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        import sys
        max_product = -sys.maxsize

        for i in range(len(nums)):
            j = i + 1
            cur = nums[i]

            while j < len(nums):
                cur = cur * nums[j]
                max_product = max(cur, max_product)
                j += 1
        return max_product

    def max(self, nums):
        if len(nums) == 1:
            return nums[0]
        import sys
        max_product = -sys.maxsize

        for i in range(len(nums)):
            j = i + 1
            cur = nums[i]
            while j < len(nums):
                cur = cur * nums[j]
                max_product = max(cur, max_product)
                j +=1

        return max_product
if __name__ == "__main__":
    print (Solution().maxProduct([2, 3, -2, 4]))
    # print (Solution().maxProduct([-4,-3]))

