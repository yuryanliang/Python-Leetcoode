# Time:  O(logn) = O(32)
# Space: O(1)
#
# Write a function that takes an unsigned integer 
# and returns the number of '1' bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, 
# so the function should return 3.
#
# 0x00000001 <<5  ---->  0x000...100000
# e.g. 1

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        for i in range(32):
            if n & (0x00000001 << i) != 0:  #<< is left move
                res += 1
        return res


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

if __name__ == '__main__':
  print Solution().hammingWeight(11)
