"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Sol:
    def long(self, s):
        res = ""
        for i in range(len(s)):
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            if (j - 1) * 2 + 1 > len(res):
                res = s[i - j + 1: i + j]

            k = 1
            while i - k >= 0 and i + k - 1 < len(s) and s[i - k] == s[i + k - 1]:
                k += 1

            if (k - 1) * 2 > len(res):
                res = s[i - k + 1: i + k - 1]
        return res


if __name__ == '__main__':
    # s = "babad"
    # s = "cbbd"
    s = "a"
    print(Sol().long(s))
