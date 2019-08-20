"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]



测试地址：
https://leetcode.com/problems/subsets/description/

"""

"""
要把每个结果sort 再加入res
permutation + 控制长度 + sort
"""

class Sol:
    def subset(self, nums):
        if not nums:
            return []
        res = [[]]
        alist =[]
        start = 0
        self.helper(nums,start,  alist, res)

        return res
    def helper(self, nums,start, alist, res):
        temp = alist.copy()
        temp.sort()
        if temp not in res:
            res.append(temp)
        # res.append(alist)
        for i  in range(start, len(nums)):
            if nums[i] not in alist:
                alist.append(nums[i])

                self.helper(nums, start + 1, alist, res)
                alist.pop()
def main():
    nums = [1, 2, 3]
    print(Sol().subset(nums))


if __name__ == '__main__':
    main()
