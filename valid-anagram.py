题目链接
https://leetcode.com/problems/valid-anagram/

题目原文
Given two strings s and t, write a function to determine if t is an anagram of s.

For example, 
s = “anagram”, t = “nagaram”, return true. 
s = “rat”, t = “car”, return false.

Note: 
You may assume the string contains only lowercase alphabets.

Follow up: 
What if the inputs contain unicode characters? How would you adapt your solution to such case?

题目翻译
给定两个字符串 s 和 t，写一个函数判断 t 是否是 s 的一个 “anagram”（颠倒字母顺序构成的词）。 
比如： s = “anagram”， t = “nagaram”，返回 true； s = “rat”， t = “car”，返回false。 
备注：假定给定的字符串都只包含小写字母。
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS = {}
        dictT = {}
        for n in s:
            if n not in dictS:
                dictS[n] = 1
            else:
                dictS[n]+=1
        for n in t:
            if n not in dictT:
                dictT[n] = 1
            else:
                dictT[n]+=1
        return dictS == dictT
进一步：如果输入包含 unicode 字符怎么办？你要怎么调整你的代码来解决这样的问题？

思路方法
思路一
比较直观的思路是，统计两个字符串中不同字符出现的次数，只有当两者出现的字符相同且出现的次数相同，那么它们是“anagram”。另外，两个长度不同的字符串一定不满足要求，可以辅助判断。 
判断字符出现次数是否相等，可以两个都统计再比较（用到两个数组），也可以一个增一个减的边统计边比较（一个数组即可）。

代码一

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        alpha = [0] * 26
        beta = [0] * 26
        for c in s:
            alpha[ord(c) - 97] += 1
        for c in t:
            beta[ord(c) - 97] += 1
        return alpha == beta
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
代码二

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        alpha = [0] * 26
        for c in s:
            alpha[ord(c) - 97] += 1
        for c in t:
            alpha[ord(c) - 97] -= 1
            if alpha[ord(c) - 97] < 0:
                return False
        return True
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
思路二
上面用数组的方法对于字符串含有 unicode 就难以处理了，所以更通用的方法应该用字典。算法与上面用数组类似。

代码

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        alpha = {}
        beta = {}
        for c in s:
            alpha[c] = alpha.get(c, 0) + 1
        for c in t:
            beta[c] = beta.get(c, 0) + 1
        return alpha == beta
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
思路三
两个字符串若是 “anagram”，则它们只是顺序不一样的相同字符的组合，那么将它们排序后比较是否相等即可。

代码

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
1
2
3
4
5
6
7
8
说明 
这里其实利用Python的排序方便了很多，但要注意 sorted(s) 返回的实际上是字符数组，所以上面代码 sorted(s) == sorted(t) 的比较是数组比较而不是字符串比较。 
这个算法对于含有 unicode 的字符串也是有效的。
