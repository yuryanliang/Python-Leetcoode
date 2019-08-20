"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""



class Sol_1:
    def plus_one(self, d):
        for i in range(len(d) - 1, -1, -1):
            if d[i] < 9:  # 结束条件，当 d[i] < 9, 把这位加一， 循环就结束。只有当前一位是9的时候，才能到这一步。除了第一步
                d[i] += 1
                return d
            d[i] = 0
        return [1] + d


def main_1():
    digits = [1, 0, 9]
    print(Sol_1().plus_one(digits))


# 末尾取余数， 取进位
class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(-1, -len(digits) - 1, -1):
            # for i in range(len(d) - 1, -1, -1):

            temp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = (temp + carry) // 10
        return [1] + digits if carry > 0 else digits


if __name__ == '__main__':
    main()
    main_1()
