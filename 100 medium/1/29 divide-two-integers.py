"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment
which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

"""

"""
用右移的方式， << 1 = * 2 **1
防止溢出         return max(min(sign * ans, 0x7fffffff), -2147483648)
reset dividend, cnt, subsum
"""
import sys

class Sol:
    def div(self, dividend, divisor):
        if divisor == 0:
            return 0x7fffffff
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        ans = 0
        cnt = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        subsum = divisor
        while dividend >= divisor:
            while (subsum << 1) <= dividend:
                cnt <<= 1
                subsum <<= 1
            ans += cnt
            dividend -= subsum # reset dividend
            cnt = 1  # reset cnt
            subsum = divisor  # reset subsum

        return max(min(sign * ans, 0x7fffffff), -2147483648)

    def div(self, dividend, divisor):
        if divisor == 0:
            return 0x7fffffff
        sign = 1

        if dividend * divisor <0:
            sign = -1

        ans = 0
        cnt = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        subsum = divisor

        while dividend >= divisor:
            while (subsum <<1) <= dividend:
                cnt <<= 1
                subsum <<= 1
            ans += cnt
            dividend -= subsum
            cnt =1
            subsum = divisor
        return max(min(sign * 0x7fffffff), -0x7fffffff+1)

def main():
    print(Sol().div(7, -3))


if __name__ == '__main__':
    main()
    print(3*(2**3))
    a =3

    # print(sys.maxsize)
    # print(0x7fffffff)
    # print(-0x7fffffff)
    # print(-2**31)
    # print(2**31-1)

