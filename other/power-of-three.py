题目原文
Given an integer, write a function to determine if it is a power of three.

Follow up: 
Could you do it without using any loop / recursion?

题目翻译
给定一个整数，判断它是否是3的倍数。 
进一步：能否不用循环或递归实现？

思路方法
思路一
先不考虑进一步的要求，用循环的做法是：每次尝试将输入的数除以3，观察是否能整除，若不能则说明不是3的倍数；若能，则用除以3的结果循环上述过程，直至得到1，说明输入是3的幂次。

代码

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1
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
思路二
先不考虑进一步的要求，用递归的做法也尝试一下。

代码

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False
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
思路三
当然，题目说了不能循环或递归，上面的解法能AC但不太符合题意。考虑到输入是“Integer”，是有范围的（<2147483648），所以存在能输入的最大的3的幂次，即 3^19=1162261467。所以只要检查输入能否被它整除即可

代码

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0
1
2
3
4
5
6
7
思路四
还可以算出能输入的所有3的幂次，保存到list或dict中，对每次输入判断是否在这些数中即可。

代码

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
        return n in nums
