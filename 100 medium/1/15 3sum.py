"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
方法一：
用for loop 循环第三个值， 另两个值做 two sum

方法二；
sort 数组
while loop 循环第三个值， 另两个值 用双指针从左右向中间移动
注意 符合条件之后的移动 要dedup
"""

class Sol:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def three_sum(self, nums):
        res = []
        for i in range(len(nums)):
            # 2 sum
            target = 0 - nums[i]
            lookup = {}
            for j in range(i +1, len(nums)):
                if target - nums[j] in lookup:
                    sol = [nums[i], nums[j], target - nums[j]]
                    sol.sort()
                    if sol not in res:
                        res.append(sol)
                else:
                    lookup[nums[j]] = j
        return res

    def three(self, nums):
        res = []
        for i in range(len(nums)):
            # 2 sum
            target = 0- nums[i]
            lookup ={}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in lookup:
                    sol = [nums[i], nums[j], target - nums[j]]
                    sol.sort()
                    if sol not in res:
                        res.append(sol)
                else:
                    lookup[nums[j]]=j
        return res

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(Sol().three_sum(nums))


if __name__ == '__main__':
    main()




class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        i = 0

        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:

                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]: # dedup, j compare to previous j
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

            i += 1

        return result

    def three(self, nums):
        nums = sorted(nums)
        result = []
        i = 0

        while i < len(nums):
            if i == 0 or nums[i] != nums[i -1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] >0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j -1]:
                            j +=1
                        while j < k and nums[k] == nums[k -1]:
                            k -= 1
            i+=1
        return result


