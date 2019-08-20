"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

"""
先判断 0行 有么有0
0列 有没有0

做上true false 标记。

处理除了0行0列的值， 在0行0列上标记

回头处理 0行 0 列

我们考虑就用原数组的第一行第一列来记录各行各列是否有0.

- 先扫描第一行第一列，如果有0，则将各自的flag设置为true
- 然后扫描除去第一行第一列的整个数组，如果有0，则将对应的第一行和第一列的数字赋0
- 再次遍历除去第一行第一列的整个数组，如果对应的第一行和第一列的数字有一个为0，则将当前值赋0
- 最后根据第一行第一列的flag来更新第一行第一列
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        for i in range(row):
            if matrix[i][0] == 0:
                first_col_zero = True

        for j in range(col):
            if matrix[0][j] == 0:
                first_row_zero = True

        for i in range(1, row):  # except the first row/col
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, row):  # except the first row/col
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0 :
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(col):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(row):
                matrix[i][0]=0

    def set(self, matrix):
        row = len(matrix)
        col = len(matrix)

        first_row_zero = False
        first_col_zero = False

        for i in range(row):
            if matrix[i][0] ==0:
                first_col_zero = True

        for j in range(col):
            if matrix[0][j] ==0:
                first_row_zero = True

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if first_row_zero:
            for j in range(col):
                matrix[0][j]=0

        if first_col_zero:
            for i in range(row):
                matrix[i][0]=0







class Sol:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for k in range(row):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "*"
                    for l in range(col):
                        if matrix[i][l] != 0:
                            matrix[i][l] = "*"
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1, 1]
        , [1, 1, 0, 1]
        , [1, 1, 1, 1]
        , [1, 1, 1, 1]]
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 3, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(matrix)
    print(matrix)
