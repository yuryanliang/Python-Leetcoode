"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Sol:
    def comb(self, candidates, target):
        if not candidates:
            return []
        res = []
        alist = []
        start = 0
        candidates.sort()
        self.helper(candidates, alist, start, target, res)

        return res
    def helper(self, can, alist,start, target, res):
        if sum(alist) == target:
            temp = alist.copy()
            temp.sort()
            if temp not in res:
                res.append(temp)
        if sum(alist) > target:
            return

        for i in range(start, len(can)):
            alist.append(can[i])
            self.helper(can, alist, start+1,target, res)
            # alist.pop()
def main():
    candidates= [2,5,2,1,2]
    target = 5
    # candidates= [1,2]
    # target = 4
    print(Sol().comb(candidates,target))


if __name__ == '__main__':
    main()
    nums =[1,2]
    path=[0,4]
    p=[0,4]
    path.append(nums[0])
    print(path== p + [nums[0]])

    1==1