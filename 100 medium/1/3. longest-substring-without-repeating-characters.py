"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
从每个字母为开头 loop一遍， 用一个指针更新最大值
edge case： 是走到头还没有重复的
"""
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    def longest(self, s):

        res = 0
        for i in range(len(s)):
            j = i + 1
            lookup = {s[i]: i} # use  dict

            while j < len(s):
                if s[j] in lookup:
                    res = max(res, j - i)
                    break
                else:
                    lookup[s[j]] = j
                j += 1
            if j == len(s):  # when s = 'au', edge case
                res = max(res, j - i)

        return res



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length

