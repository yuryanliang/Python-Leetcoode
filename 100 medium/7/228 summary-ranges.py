"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res

        start, end = nums[0], nums[0]
        for i in range(1, len(nums)+1):
            if i< len(nums) and nums[i] == end +1:
                end = nums[i]
            else:
                interval =str(start)
                if start != end:
                    interval += "->" + str(end)
                res.append(interval)
                if i < len(nums):
                    start = end = nums[i]
        return res

    def summ(self,nums):
        res = []
        if not nums:
            return res

        start, end = nums[0], nums[0]

        for i in range(1, len(nums)+ 1):
            if i < len(nums) and nums[i]==end +1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->"+str(end)
                res.append(interval)

                if i < len(nums):
                    start = end = nums[i]
        return res




if __name__ == '__main__':
    nums =[0,1,2,4,5,7]
    # nums =[0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))

