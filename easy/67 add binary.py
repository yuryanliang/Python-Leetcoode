class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = '0' * (len(b) - len(a)) + a
        b = '0' * (len(a) - len(b)) + b
        # print('a',a,b)

        carry, result = 0, ''
        for i in range(len(a) - 1, -1, -1):
            ans = int(a[i]) + int(b[i]) + carry
            if ans > 1:
                carry = 1
                ans %= 2
            else:
                carry = 0
            result = str(ans) + result
        # print(result)
        if carry:
            result = '1' + result
        return result

# class Solution:
# 	def addBinary(self, a: str, b: str) -> str:
#
#         def findNum(string):
#             k, number = 0, 0
#             for i in range(len(string)-1,-1,-1):
#                 number += int(string[i]) * (2**k)
#                 k += 1
#             return number
#     # return bin(findNum(a) + findNum(b))[2:]