"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

"""
因为有重复的数 ， 所以需要做一个used 的 备份表， 每次加数字之前看看有没有用过。 
从第二个开始，即（i>0)，如果后一个数跟前面的一样，并且没用过，要掠过
"""

class Solution:
    def permuteUnique(self, nums):
        res = []
        alist = []
        used = [False] * len(nums)
        self.helper(nums, used, alist, res)

        return res

    def helper(self, nums, used, alist, res):

        if len(alist) == len(nums) and alist not in res:
            res.append(list(alist))
            return

        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                used[i] = True
                alist.append(nums[i])

                self.helper(nums, used, alist, res)
                alist.pop()
                used[i] = False

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(result, used, [], nums)
        return result

    def permuteUniqueRecu(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur + [])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i - 1] == nums[i] and not used[i - 1]):
                continue
            used[i] = True
            cur.append(nums[i])
            self.permuteUniqueRecu(result, used, cur, nums)
            cur.pop()
            used[i] = False




def main():
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))


if __name__ == '__main__':
    main()
