"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution:
    def canJump(self, nums):
        if len(nums)==1:
            return True
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        # dp[1]= max(dp[0], nums[0]) -1
        #     = 1
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], nums[i-1]) - 1
            if dp[i] < 0:
                return False
        return True


"""
        2, 3, 1, 1, 4.
        dp[i]
        dp[1]= dp[0] - (1-0)
        dp[2]=max(nums[1], dp[1])-1
        
        
        """


class Sol:
    def canJump(self, nums):
        n = len(nums)
        reach = 0
        for i in range(n):
            if i > reach or reach >= n-1:
                break
            reach = max(reach , i + nums[i])
        return reach >= n -1




if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    nums = [0]
    nums = [0,2,3]


    print(Sol().canJump(nums))
