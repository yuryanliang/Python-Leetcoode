# Time:  O(n)
# Space: O(1)

# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order 
# of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after 
# calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
'''解题思路：
题目可以在O(n)时间复杂度内求解

算法步骤：

使用两个"指针"x和y，初始令y = 0

利用x遍历数组nums：

若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

算法简析：

y指针指向首个0元素可能存在的位置

遍历过程中，算法确保[y, x)范围内的元素均为0'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
题目翻译
给定一个数组，写一个函数，将数组中的0都移动到数组末尾，同时保持非零数字的顺序。 
比如，数组nums=[0, 1, 0, 3, 12]，调用你的函数后，数组变成[1, 3, 12, 0, 0]。 
注意： 
1. 你必须在原数组上进行修改，不能拷贝一个新数组； 
2. 尽量减少你的操作次数。

思路方法
思路一
从后向前搜索，把找到的0都移动到最后，即，将找到的0后面的非零数向前移动。

代码

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] == 0:
                for j in xrange(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[j-1] = nums[j]
                        nums[j] = 0
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
思路二
上面的算法效率太低，考虑将每个非零的数都移动到前面一个非零数的后面。 
维持两个指针，慢的指针始终指向上一个非零数的后面，快指针向后扫描直至找到一个非零数，将快指针找到的非零数赋值给慢指针的位置后将慢指针后移一个位置，同时将快指针所在处的数置为0。循环下去即可。

代码一

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1
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
该思路下，也可以先将所有的非零数移动到前面，再一次性将后面所有数置为0。这样需要用到两个循环。

代码二

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in xrange(i, len(nums)):
            nums[j] = 0
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
思路三
当然，用Python写代码，还可以用一些比较tricky的方法，比如用自带的sort函数也可以AC。但我并不确定sort函数会不会申请一个临时数组，所以该方法不一定满足题意，但仍然可供我们学习。

代码

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key = lambda x: 1 if x == 0 else 0)
