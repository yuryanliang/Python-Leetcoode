"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

"""
# O(n) while loop
class Sol_1:
    def insert(self, nums, target):
        # if len(nums) == 0 or target < nums[0]:
        #     return 0

        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i


# O(n) for loop
class Sol_1_1:
    def insert(self, nums, target):
        # if len(nums) == 0 or target < nums[0]:
        #     return 0

        i = 0
        for i in range(len(nums)):
            if nums[i] >= target:  # first >= target
                return i
        return len(nums)


# binary search O(logn)
class Sol_2:
    def insert(self, nums, target):  # target = 7
        # edge case
        if nums[-1] < target:
            return len(nums)

        left = 0  # left = 3
        right = len(nums) - 1  # right = 3

        while left < right:
            mid = (left + right) // 2  # mid = 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


def main():
    nums = [1, 3, 5, 6]
    print(Sol_2().insert(nums, 7))


if __name__ == '__main__':
    main()
