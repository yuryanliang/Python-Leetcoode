"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

"""
用i + 1， 而不是ind 加一。来略过已经用过的值
"""

class Solution:
    def subsetsWithDup(self, nums) :

        res = []
        path =[]
        ind = 0
        self.helper(nums, res, path, ind)
        return res
    def helper(self, nums, res, path, ind):
        temp = list(path)
        res.append(temp)

        # temp.sort()
        # if temp not in res:
        #     res.append(temp)
        cur_index = ind

        for i in range(ind, len(nums)):
            path.append(nums[i])
            self.helper(nums, res, path, i + 1)
            path.pop()

class Sol:
    def sub(self, nums):
        res = []
        path = []
        ind = 0

        self.helper(nums, res, path, ind)
        return res

    def helper(self, nums, res, path, ind):
        res.append(list(path))

        for i in range(ind, len(nums)):
            path.append(nums[i])
            self.helper(nums, res, path, i + 1)
            path.pop()


def main():
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()