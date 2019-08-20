'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Sol_1:
    def strStr(self, haystack, needle):

        if not needle:
            return 0

        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle):
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == len(needle):
                    return i
            i += 1
        return -1


def main_1():
    haystack = "aaabaaabbbabaa"
    needle = "babb"
    needle = "aba"
    print(Sol_1().strStr(haystack, needle))
    print(Sol().strstr(haystack, needle))


class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        elif not needle in haystack:
            return -1


if __name__ == '__main__':
    main_1()
