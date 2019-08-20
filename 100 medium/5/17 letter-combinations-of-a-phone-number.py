"""

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
"""
DFS 中 什么时候用if else; 什么时候用 if return?
如果用了if else 就不用return。 用了return， 就不用else

DFS 中 什么时候用pop?
如果path是list， 需要用 append 加新元素， 不能把append 和 dfs 写在一行时候，要单调用pop
如果path是string， 可以直接在dfs一行处理，就不用pop



"""

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]

        for digit in digits:
            choices = lookup[int(digit)]
            n = len(res)
            res = res * len(choices)
            for i in range(len(choices) * n):
                temp = i // n
                res[i] = res[i] + choices[temp]
        return res

    def letter(self, digits):
        if not digits:
            return []
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]

        for d in digits:
            choices = lookup[int(d)]
            n = len(res)
            res = res * len(choices)
            for i in range(len(choices)* n):
                temp = i //n
                res[i]= res[i]+ choices[temp]
        return res



class Solution2(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        path = ""
        index = 0
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                  "pqrs", "tuv", "wxyz"]
        self.helper(digits, res, path, lookup, index)
        return res

    def helper(self, digits, res, path, lookup, index):
        if index == len(digits):
            res.append(path)
        else:
            for choice in lookup[int(digits[index])]: #if there is NOT append, then no need to pop
                # 方案一， path + choice 单独在一行，后面需要pop
                path = path + choice
                self.helper(digits, res, path , lookup, index + 1)
                path = path[:-1]

                #方案二， path + choice 写到了 DFS 里面， 就不用写pop
                self.helper(digits, res, path + choice, lookup, index + 1)

#
class Solution3(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                  "pqrs", "tuv", "wxyz"]

        res = []
        path = []
        index = 0
        self.dfs(digits, res, path, lookup, index )
        return res

    def dfs(self, digits, res, path, lookup, index):
        if index  == len(digits):
            res.append("".join(path))
            return

        for choice in lookup[int(digits[index])]:  # if need append, then remember to pop
            path.append(choice)
            self.dfs(digits, res, path , lookup, index + 1)
            path.pop()


if __name__ == '__main__':
    digits = "23"
    print(Solution2().letterCombinations(digits))
