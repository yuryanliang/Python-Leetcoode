"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
# brute force
class Sol_1:
    def sqrt_1(self, n):  # n = 7
        if n < 0:
            return -1

        # find the sqrt
        i = 0
        while i ** 2 <= n:  # i = 2
            i += 1
        i = i - 1

        return i


def main_1():
    nums = [-1, 1, 5, 4, 7, 8]
    for i in nums:
        print(Sol_1().sqrt_1(i))


# binary search
class Sol_2:
    def sqrt_2(self, n):  # n = 7
        if n < 2:
            return n

        left = 0
        right = n

        while left < right:  # i = 2
            mid = (left + right ) // 2
            if mid ** 2 == n:
                return mid
            elif mid ** 2 < n:
                left = mid + 1
            else:
                right = mid
        return left - 1  # left is the first one >= n, so left - 1



def main_2():
    nums = [-1, 1, 3, 4, 8]
    for i in nums:
        print(i,Sol_2().sqrt_2(i))


if __name__ == '__main__':
    # main_1()
    main_2()
