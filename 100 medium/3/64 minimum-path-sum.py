"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

"""
二维dp问题。 dp[i][j]= grid[i][j] + min(dp[i-1][j], dp[i][j - 1])
如果过界， 把值设为maxsize
跳过初始点


"""

import sys
class Solution:
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])

        dp = [[-1 for _ in range(col)] for _ in range(row)]

        dp[0][0] = grid[0][0]

        for i in range(row):
            for j in range(col):

                up = dp[i - 1][j] if 0 <= i - 1 else sys.maxsize
                left = dp[i][j - 1] if 0 <= j - 1 else sys.maxsize
                if i == 0 and j == 0   :
                    continue
                else:
                    dp[i][j] = grid[i][j] + min(up, left)
        return dp[row-1][col-1]

    def min(self, grid):
        row =len(grid)
        col = len(grid[0])

        dp = [[-1 for _ in range(col)] for _ in range(row)]

        dp[0][0]= grid[0][0]

        for i in range(row):
            for j in range(col):
                up = dp[i-1][j] if i -1 >=0 else sys.maxsize
                left = dp[i][j -1] if j -1 >=0 else sys.maxsize

                if i == 0 and j == 0:
                    continue
                else:
                    dp[i][j]= grid[i][j] + min(up, left)
        return dp[row -1][col -1]


class Solution(object):
    def get_up_left(self, x, y):
        if y - 1 < 0:
            up = False
        else:
            up = (x, y - 1)
        if x - 1 < 0:
            left = False
        else:
            left = (x - 1, y)

        # up and left
        return (up, left)

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                xy = self.get_up_left(j, i)
                up = grid[xy[0][1]][xy[0][0]] if xy[0] else float('inf')
                left = grid[xy[1][1]][xy[1][0]] if xy[1] else float('inf')

                if up == float('inf') and left == float('inf'):
                    continue
                grid[i][j] = grid[i][j] + min(up, left)

        return grid[-1][-1]

if __name__ == "__main__":
    # print(Solution().minPathSum([[0, 1]
    #                                 , [1, 0]]))
    print(Solution().minPathSum([[1, 3, 1]
                                    , [1, 5, 1]
                                    , [4, 2, 1]]))




# class Solution:
#     def minPathSum(self, grid):
#         res = []
#         cur_sum = 0
#         i = 0
#         j = 0
#         row = len(grid)
#         col = len(grid[0])
#         visited=[[False for _ in range(col)] for _ in range(row)]
#
#         self.helper(grid, res, cur_sum, i, j, row, col, visited)
#
#         return min(res)
#
#     def helper(self, grid, res, cur_sum, i, j, row, col, visited):
#         if i == row - 1 and j == col - 1:
#             cur_sum += grid[i][j]
#
#             res.append(cur_sum)
#             return
#         if i < row and j  <col and not visited[i][j]:
#             visited[i][j]= True
#             print(i, j)
#             cur_sum += grid[i][j]
#
#
#             self.helper(grid, res, cur_sum , i +1, j, row, col,visited)
#             visited[i][j]= False
#             self.helper(grid, res, cur_sum , i, j+1, row, col, visited)
#             visited[i][j]= False

