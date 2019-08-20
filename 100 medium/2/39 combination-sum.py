"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
"""
backtracking
初始 res， 也许start， path

进入helper， 先判断什么时候加结果， len（path）= len（nums） 或者直接就加， 要考虑dedup 要copy temp

然后for loop，从start或者i开始， 先加入path。 然后call helper， 然后pop
"""
class Sol:
    def comb_sum(self, candidates, target):
        if not candidates:
            return []
        result = []
        path = []  # nums already used
        start = 0 # need to use a start point otherwise it exceed time limit
        self.helper(candidates, start, path, target, result)
        return result

    def helper(self, cand, start, path, target, res):
        if sum(path) == target:
            temp = path.copy()
            temp.sort()
            if temp not in res:
                res.append(temp)

        while start < len(cand) and sum(path) < target:
            path.append(cand[start])
            self.helper(cand, start, path, target, res)
            path.pop()
            start += 1


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0: # 因为是不重复数组，所以不用担心dedup
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            # below， 可重复用cand， 所以还是start； 不可重复， start + 1
            self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1

"""
comb sum II
"""
class Solution_2:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return set(result)

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0 and intermediate not in result: #删掉pre， 用 这个判断dedup，
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            # pre 是防止在有【1， 1】的情况下，对每一个1 都进行dfs， 我们也可以用别的方式dedup
            intermediate.append(candidates[start])
            # below， 可重复用cand， 所以还是start； 不可重复， start + 1
            self.combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1




def main():
    candidates = [2, 3, 6, 7]
    target = 7
    print(Sol().comb_sum(candidates, target))


if __name__ == '__main__':
    main()
