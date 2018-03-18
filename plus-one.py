# Time:  O(n)
# Space: O(1)

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# in-place solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else: 
                digits[i] += 1
                return digits
            i -=1
        
        if i == -1:
            return [1] + digits
        else: 
            return digits
