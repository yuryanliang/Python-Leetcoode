"""思路一
为方便打开思路，先不考虑“Follow up”的要求。不能用除法，还要求O(n)的时间复杂度，那么乘法不能做的太过。考虑先正反两次遍历，一次遍历求每个数左侧的所有数的积，一次遍历求每个数右侧的所有数的积，最后两部分积相乘即得所求。 
下面的代码使用了额外的两个数组，空间复杂度O(n)"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, leftMul, rightMul = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        leftMul[0] = rightMul[len(nums)-1] = 1
        for i in range(1, len(nums)):
            leftMul[i] = leftMul[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rightMul[i] = rightMul[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = leftMul[i] * rightMul[i]
        return res
        
  """思路二
在上面的基础上，实际上用数组存储左右的积并不必要，用临时变量即可，于是有下面的O(1)空间复杂度的解法。"""   
        
        
        class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        tmp = 1
        for i in xrange(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in xrange(len(nums)-1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res
