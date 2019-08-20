"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
 prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
 find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
from collections import defaultdict


class Sol:
    def dup(self, nums):
        lookup = defaultdict(list)
        for i, val in enumerate(nums):
            if val in lookup:
                return val
            else:
                lookup[val].append(i)

class Sol:
    def dup(self, nums):
        lookup = defaultdict(list)
        for i, val in enumerate(nums):
            if val in lookup:
                return val
            else:
                lookup[val].append(i)


# binary
class Sol1:
    def dup(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left


# fast, slow pointer

# https://blog.csdn.net/monkeyduck/article/details/50439840
class Sol2:
    def dup(self,nums):
        slow = nums[0]
        fast= nums[nums[0]]

        while fast != slow:
            slow= nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow=nums[slow]
        return slow
if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(Sol2().dup(nums))
