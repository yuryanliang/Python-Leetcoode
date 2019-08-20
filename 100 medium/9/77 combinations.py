"""

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


"""


class Sol_1:
    def combine(self, n, k):
        nums = list(range(1, n + 1))
        return self.helper(nums, k)

    def helper(self, nums, r):
        if r == 1:
            return [[num] for num in nums]
        if len(nums) == r:
            return [nums]
        output = []
        for index in range(len(nums) - r + 1):
            for remainder in self.helper(nums[index + 1:], r - 1):
                output.append([nums[index]] + remainder)
        return output



class Sol_2:

    def combine(self, n, k):
        def _dfs(n, k, path, list_ret):
            # I am done with this combination, add to result
            if len(path) + 1 == k:
                list_ret.append([n] + path)
                return
            # Not done yet, construct path that includes this number
            for i in range(n - 1, 0, -1):
                _dfs(i, k, [n] + path, list_ret)

        list_ret = []
        if n < k or n == 0:
            return []
        k = 1 if k == 0 else k
        # Combinations may end from any number ranging from k to n
        # At the beginning, path is empty
        for i in range(k, n + 1):
            _dfs(i, k, [], list_ret)
        return list_ret


def main():
    n = 3
    k = 2
    print(Sol_1().combine(n, k))


if __name__ == '__main__':
    main()


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result, combination = [], []
        i = 1
        while True:
            if len(combination) == k:
                result.append(combination[:])
            if len(combination) == k or \
                    len(combination) + (n - i + 1) < k:
                if not combination:
                    break
                i = combination.pop() + 1
            else:
                combination.append(i)
                i += 1
        return result


class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def combineDFS(n, start, intermediate, k, result):
            if k == 0:
                result.append(intermediate[:])
                return
            for i in xrange(start, n):
                intermediate.append(i + 1)
                combineDFS(n, i + 1, intermediate, k - 1, result)
                intermediate.pop()

        result = []
        combineDFS(n, 0, [], k, result)
        return result


