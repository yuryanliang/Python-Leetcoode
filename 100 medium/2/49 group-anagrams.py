"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

"""
把每一个sort 过的str 做成key， 把str 做成value

用try except 做append 或者附上新值
"""
class Solution:
    def groupAnagrams(self, strs) :
        result = {}

        for i in strs:
            key = ''.join(sorted(i))

            try:
                result[key].append(i)
            except:
                result[key] = [i]

        return result.values()

    def g(self,strs):
        res={}
        for s in strs:
            key = ''.join(sorted(s))
            try:
                res[key].append(s)
            except:
                res[key]=[s]
        return res.values()




if __name__ == "__main__":
    result = Solution().groupAnagrams(["cat", "dog", "act", "mac"])
    print (result)