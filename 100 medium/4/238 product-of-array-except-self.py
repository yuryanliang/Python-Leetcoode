"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)


"""


class Solution:
    def productExceptSelf(self, nums) :
        n = len(nums)
        res = [0 for _ in range(n)]
        fwd = [1 for _ in range(n)]
        bwd = [1 for _ in range(n)]
        fwd[0] = 1
        bwd[n-1] =1

        for i in range(1, n):
            fwd[i]= fwd[i -1] * nums[i - 1]

        for j in reversed(range(0, n-1)):
            bwd[j]= bwd[j + 1] * nums[j + 1]
        for k in range(n):
            res[k] = fwd[k] * bwd[k]
        return res


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if not nums:
            return []

        left_product = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product

        return left_product
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))


