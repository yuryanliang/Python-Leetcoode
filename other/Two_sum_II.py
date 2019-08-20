# Time:  O(n)
# Space: O(1)
#
# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 
        right = len(numbers)-1
        
        while left != right:
            sum = numbers[left]+ numbers[right]
            if sum > target:
                right -=1
            elif sum < target:
                left +=1
            else:
                return [left+1, right+1]
                
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map={}
        
        for i  in range(len(numbers)):
            if target - numbers[i] in num_map:
                return (num_map[target - numbers[i]]+1, i+1)
            else:
                num_map[numbers[i]] = i
        
