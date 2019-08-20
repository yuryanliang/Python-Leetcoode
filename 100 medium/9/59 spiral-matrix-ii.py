"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Sol:
    def spiral(self, n):
        matrix = [[ 0 for _ in range(n)] for _ in range(n)]

        left, right = 0, n -1
        top, bottom = 0, n - 1

        x = 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                matrix[top][i] = x
                x +=1
            for j in range(top +1, bottom):
                matrix[j][right] = x
                x +=1

            for i in reversed(range(left, right + 1)):
                if left < right:
                    matrix[bottom][i] =x
                    x +=1
            for j in reversed(range(top + 1, bottom)):
                if top < bottom:
                    matrix[j][left] = x
                    x +=1

            left +=1
            right -=1
            top +=1
            bottom -= 1

        return  matrix
if __name__ == '__main__':
    print(Sol().spiral(3))
