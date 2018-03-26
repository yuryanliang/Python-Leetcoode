# Time:  O(n)
# Space: O(n)

# Design and implement a TwoSum class. It should support the following operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
# 
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
class TwoSum:

    def __init__(self):
        self.nums = {}
        """
        Initialize your data structure here.
        """
        
    def add(self, number):
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        
    def find(self, value):
        nums = self.nums
        for n in nums:
            if value - n in nums and (value - n != n or nums[n] >= 2):
                return True
                
        return False
    
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        
from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.lookup = defaultdict(int)
        


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.lookup[number] += 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (num != key or self.lookup[key] > 1):
                return True
        return False


if __name__ == "__main__":
    Sol = TwoSum()
    
    for i in (1, 3, 5):
        Sol.add(i)
    
    for i in (4, 7):
        print Sol.find(i)
