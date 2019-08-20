"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

"""
DFS/backtracking 类似permutation 
1 找到所有的拆分方案
2。 看看每个part 是不是回文
3。 整体dfs。 backtracking

注意， 在helper 里面， 当i = len（s）

"""

class Solution:
    def partition(self, s: str):

        res = []
        i = 0  # starting index of substr
        cur = []
        self.helper(s, res, cur, i)
        return res

    def helper(self, s, res, cur, i):
        if i == len(s):
            res.append(list(cur))
        else:
            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j + 1]):
                    cur.append(s[i:j + 1])
                    self.helper(s, res, cur, j + 1)
                    cur.pop()

    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
