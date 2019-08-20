"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
class Solution:
    def gameOfLife(self, board) :
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.check(board, i, j)
                if board[i][j]==0:
                    if count ==3:
                        board[i][j]=2
                elif board[i][j] ==1:
                    if count <2 or count >3:
                        board[i][j]=-1
        # for l in board:
        #     print(l,)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== -1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
        # for l in board:
        #     print(l,)





    def check(self, board, i, j):
        count = 0
        for x in [i-1, i, i + 1]:
            for y in [j-1, j, j +1]:
                if not(x ==i and y ==j):
                    if  (x >= 0 and x < len((board))) and y >=0 and y < len(board[0]):

                        if board[x][y]==1 or board[x][y]==-1:
                            count +=1
        return count


if __name__ == '__main__':
    board =[
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    # print(Solution().check(board, 2, 0))
    print(Solution().gameOfLife(board))

