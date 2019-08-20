"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""


# brute force
# space complexity (n)
class Sol:
    def max_sub(self, nums):
        if not nums:
            return 0
        import sys
        max_sum = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                max_sum = max(max_sum, sum(nums[i:j]))
        return max_sum


# best
class Sol_2:
    def max_subarray(self, nums):
        # if len(nums) == 0:
        #     return 0
        cur = 0
        import sys
        max_sum = -sys.maxsize

        for i in range(0, len(nums)):
            # if cur < 0: # 一旦前面总和<0,说明前面的加进去也是没用的，所以全部抛弃
            cur = max(nums[i], cur + nums[i])  # 放弃cur，只取num，和不放弃cur，取num哪个大。
            max_sum = max(max_sum, cur)
        return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    nums_1 = [-1, 2]
    # res = Sol_1().maxSubArray(nums)
    # res = Sol_2().max_subarray(nums)
    res_1 = Sol_2().max_subarray(nums)
    # res_1 = Sol().max_sub(nums)
    # print(res)
    print(res_1)


if __name__ == '__main__':
    main()
