Given numRows, generate the first numRows of Pascal’s triangle.

For example, given numRows = 5, 
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
1
2
3
4
5
6
7
题目翻译
给定数字的行数numRows，生成帕斯卡三角形的前numRows行。比如，给定numRows=5，返回：

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
1
2
3
4
5
6
7
思路方法
首先，你要知道帕斯卡三角形的规律： 
它是一个三角形矩阵，其顶端第0行是 1；第1行两个1，这两个1是由他们上头左右两数之和 (不在三角形内的数视为0)。依此类推产生第2行：0+1=1；1+1=2；1+0=1。第3行：0+1=1；1+2=3；2+1=3；1+0=1。循此产生后面的行。

思路一
直接按照上面的规律，每一行的数据都是新生成的。这里要注意判断不在三角形内的数要视为0。

代码

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                res[i].append((res[i-1][j-1] if j>0 else 0) + (res[i-1][j] if j<i else 0))
        return res
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
思路二
实际上，每一行的第一和最后一个数都是1，考虑到这一点可以稍微减少计算量，同时避免了对额外情况的判断和处理。

代码

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0, numRows):
            res.append([1]*(i+1))
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
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
思路三
利用python的map函数可以比较精简的实现该算法。这里用到一个小小的trick，即：每一行的结果可以由上一行和上一行的偏移相加得到。例如：

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1 
1
2
3
代码

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
