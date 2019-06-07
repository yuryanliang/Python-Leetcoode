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

class Solution:
    def hammingWeight(self,n):
        res =0
        for i in range(32):
            if
