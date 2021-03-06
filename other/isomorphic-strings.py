思路二
类似上面的思路，为了避免在最后对hashmap中的值做“是否有重复”的判断，在遍历s和t的时候将已经经过映射的值保存在mapval这个dict中，这样在中途发现重复时也可以及时返回false。

代码

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        mapval = {}
        for i in xrange(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            elif t[i] in mapval:
                return False
            else:
                hashmap[s[i]] = t[i]
                mapval[t[i]] = True
        return True
        
# Time:  O(n)
# Space: O(1)

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. No two characters may map to 
# the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

from itertools import izip  # Generator version of zip.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for p, w in izip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w 
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
    
        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True
        
        
        
 题目原文
Given two strings s and t, determine if they are isomorphic. 
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example, 
Given “egg”, “add”, return true. 
Given “foo”, “bar”, return false. 
Given “paper”, “title”, return true.

Note: 
You may assume both s and t have the same length.

题目翻译
给定两个字符串，判断它们是否是同构的。如果一个字符串s中的字符可以替换成别的字符，从而得到另一个字符串t，那么两个字符串同构。 
字符串中所有的一样的字符都要替换，并且要保持原顺序。两个不同的字符不能替换成相同的字符，一个字符可以替换成它自己。

比如： 
给定 "egg", "add", 返回 true 
给定 "foo", "bar", 返回 false 
给定 "paper", "title", 返回 true

注意：假设两个字符串s和t的长度相同。

思路方法
思路一
先遍历一遍s和t，将s到t的字符映射存放在dict中，遍历过程中如果发现某个位置的映射与已经确定的映射冲突则可以直接返回false。但这个过程无法发现“不同的字符映射到相同的字符”这一情况，所以最后还要判断得到的映射关系是否有重复。

代码

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in xrange(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        mapval = [hashmap[k] for k in hashmap]
        return len(mapval) == len(set(mapval))
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
思路二
类似上面的思路，为了避免在最后对hashmap中的值做“是否有重复”的判断，在遍历s和t的时候将已经经过映射的值保存在mapval这个dict中，这样在中途发现重复时也可以及时返回false。

代码

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        mapval = {}
        for i in xrange(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            elif t[i] in mapval:
                return False
            else:
                hashmap[s[i]] = t[i]
                mapval[t[i]] = True
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
19
思路三
对于s和t，分别用一个数组记录每个字符在该字符串中上一次出现的位置。当同时遍历s和t时，如果发现它们在某一位置的字符上次出现的位置不同，则返回false。

代码

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos1, pos2 = [-1]*256, [-1]*256
        for i in xrange(len(s)):
            if pos1[ord(s[i])] != pos2[ord(t[i])]:
                return False
            pos1[ord(s[i])] = pos2[ord(t[i])] = i
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
思路四
与思路三类似，相当于思路三记录上次出现位置，而现在记录第一次出现的位置。 
对于s，遍历将其每个字符第一次出现的位置记录成一个新的数组；对t做同样的处理。如果得到的两个数组相同，则说明这是一个符合要求的映射，s和t同构；否则不同构。 
用Python的内置函数map和字符串的find函数，可以一行实现。

代码

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.find, t)
1
2
3
4
5
6
7
8
思路五
根据题目描述的映射要求，s有多少种不同的字符，t也有多少种不同的字符。如果我们将映射写成字符对的形式，比如 (‘a’,’c’) 表示s中字符’a’映射到t中’c’，那么映射的个数与s中字符的种类数相同。 
用Python的内置函数zip，也可以一行实现判断同构。

代码

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
