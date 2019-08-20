"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
每个字母为中心loop一遍

内层while 循环同时向两边扩展

分 single 和double 两种情况
"""


class Solution:
    # def longestPalindrome(self, s: str) -> str:
    def longest(self, s):
        res = 0
        for i in range(s):
            j = 1
            while 0 < j < len(s):
                if s[i] == s[i + 1]:  # double
                    if s[i + 1 + j] != s[i - j]:
                        res = max(res, (j * 2))
                        break

                else:  # single
                    if s[i + j] != s[i - j]:
                        res = max(res, (j * 2 - 1))
                        break
                j += 1

        return res

    def longest(self,s):
        res =0
        for i in range(s):
            j = 1
            while 0<j<len(s):
                #double
                if s[j]==s[j + 1]:
                    if s[i + 1 + j] != s[i - j]:
                        res = max(res, j * 2)
                        break
                else:
                    #single
                    if s[i + j ]!=s[i -j]:
                        res = max(res, j * 2 -1)
                        break

                j += 1
        return res

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            if 2 * (n - i) + 1 < right - left + 1:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return s[left:right + 1]
