"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""


# https://leetcode.com/problems/valid-sudoku/

class Sol1:
    def sudoku(self, board):
        for i in range(9):

            if not self.valid(board[i][j] for j in range(9)):
                return False
            a =[board[j][i] for j in range(9)]
            if not self.valid(board[j][i] for j in range(9)):
                return False

            # in 1 line
            if not self.valid([board[i][j] for j in range(9)]) \
                    or not self.valid([board[j][i] for j in range(9)]):
                return False

        for i in range(3):
            for j in range(3):
                b =[board[m][n] for m in range(3 * i, 3 * i + 3) for n in range(3 * j, 3 * j + 3)]
                if not self.valid([board[m][n] for m in range(3 * i, 3 * i + 3) for n in range(3 * j, 3 * j + 3)]):
                    return False

        return True
    def valid(self, area):
        temp= filter(lambda x:x != ".", area)
        area=tuple(temp)
        return len(set(area)) == len(area)
class Sol:
    def sudoku(self, board):
        if not board or not board[0]:
            return False

        # row
        for i in board:
            if not self.valid(i):
                return False

        # col
        for j in range(9):
            area = []
            for k in range(9):
                area.append(board[k][j])
            if not self.valid(area):
                return False

        # square
        for k in [0, 3, 6]:
            for l in [0, 3, 6]:
                area = []
                for i in range(k, k + 3):
                    for j in range(l, l + 3):
                        area.append(board[i][j])
                if not self.valid(area):
                    return False
        return True

    def valid(self, area):
        lookup = {}
        for i in area:
            if i != ".":
                if i in lookup and lookup[i] == 1:
                    return False
                else:
                    lookup[i] = 1
        return True


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Sol1().sudoku(board))
