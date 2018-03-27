题目链接
https://leetcode.com/problems/plus-one/

题目原文
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

题目翻译
给定一个用数组表示的非负数，对这个数加一。这个数组里的数字最高位在列表头部。

思路方法
这个题目有点难理解，应该举个例子的。。。大概就是，比如： 
数字1234用数组表示是[1,2,3,4]，加一后数组表示为[1,2,3,5]；数字9999用数组表示是[9,9,9,9]，加一得到[1,0,0,0,0]。

思路一
从后向前扫描数组，每位加一，有进位则变成0且保留进位。最高位如果是9且有进位则要在数组前面多加一个元素1。

class Solution(object):
    def plusOne(self, d):
        for i in range(len(d)-1, -1, -1):
            if d[i] < 9:
                d[i] += 1
                return d
            d[i] = 0
        return [1] + d
    
    
代码

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + plus > 9:
                digits[i] = 0
                plus = 1
            else:
                digits[i] = digits[i] + plus
                plus = 0
        if plus == 1:
            digits.insert(0, 1)
        return digits
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
思路二
当然，实际上完全不用全部数字都做判断，小于等于8的数字加一后就可以终止了。

代码

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits
    
    # Time:  O(n)
# Space: O(1)

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# in-place solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else: 
                digits[i] += 1
                return digits
            i -=1
        
        if i == -1:
            return [1] + digits
        else: 
            return digits
