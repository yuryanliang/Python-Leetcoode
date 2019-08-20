"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""


class Sol:
    def pattern(self, pattern, str):
        from collections import defaultdict
        lookup = defaultdict(list)
        i = 0
        str_list = str.split()
        if len(pattern) ==1 and len(str_list)==1:
            return True

        if len(pattern) != len(str_list):
            return False
        while i < len(pattern):
            if pattern[i] in lookup:
                if lookup[pattern[i]] != str_list[i]:
                    return False
            else:
                if str_list[i] in lookup.values():
                    return False
                lookup[pattern[i]] = str_list[i]
            i += 1
        return True


if __name__ == '__main__':
    # pattern = "abba"
    # str = "dog cat cat dog"
    pattern = "jquery"
    str = "jquery"
    # pattern = "abba"
    # str = "dog dog dog dog"
    # pattern = "aaa"
    # str = "aa aa aa aa"

    # pattern= "e"
    # str ="eukera"
    print(Sol().pattern(pattern, str))
