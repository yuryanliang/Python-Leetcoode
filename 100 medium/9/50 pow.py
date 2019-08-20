"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""
# brute force
class Sol_1:
    def pow(self, x, n):
        n1 = n if n > 0 else -n
        res = 1
        for i in range(n1 ):
            res = res *x
        return res if n > 0 else 1 / res


def main_1():
    print(Sol_1().pow(2.00000, -2))
    print(Sol_1().pow(2.10000, 3))
    print(Sol_1().pow(2.00000, 10))

# recursion
class Sol_2:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        half = self.pow(x, n // 2)

        if n % 2 ==0:
            return half ** 2
        else:
            return half ** 2 * x



def main_2():
    print(Sol_2().pow(2.00000, -2))
    print(Sol_2().pow(2.10000, 3))
    print(Sol_2().pow(2.00000, 10))
    # print(Sol_2().pow(-2, ))


if __name__ == '__main__':
    # main_1()
    main_2()
