# Time:  O(n)
# Space: O(1)
#
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aIndex = len(a) - 1
        bIndex = len(b) - 1
        flag = 0
        s = ''
        
        while aIndex >= 0 and bIndex >= 0:
            num = int(a[aIndex]) + int(b[bIndex]) + flag
            flag = num / 2
            num %= 2
            s = str(num) + s
            aIndex -=1
            bIndex -=1
            
        while aIndex >= 0:
            num = int(a[aIndex]) + flag
            flag = num / 2
            num %= 2
            s = str(num) + s
            aIndex -=1   
        
        while bIndex >= 0:
            num = int(b[bIndex]) + flag
            flag = num / 2
            num %= 2
            s = str(num) + s
            bIndex -=1
        if flag == 1:
            s = '1' + s
        return s
