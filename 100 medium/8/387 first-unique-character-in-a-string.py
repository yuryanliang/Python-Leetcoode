"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Sol:
    def non_rep(self, s):
        from collections import defaultdict
        lookup = defaultdict()
        candidate = set()
        for i, c in enumerate(s):
            if c in lookup:
                candidate.discard(lookup[c])
            else:
                lookup[c]=i
                candidate.add(i)

        return min(candidate) if candidate else -1


if __name__ == '__main__':
    s = "abcabe"
    Sol().non_rep(s)