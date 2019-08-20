"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Sol:
    def wiggle(self, nums):
        temp = nums
        temp.sort()
        t = (len(temp) +1)// 2

        head= temp[:t]
        tail = temp[t:]
        i = 0
        j = 0
        k = len(nums)-1
        while k>=0:
            if not k % 2:
                nums[k] = head[i]
                i+=1
            else:
                nums[k] = tail[j]
                j+=1

            k-=1


if __name__ == '__main__':
    # nums = [1, 5, 1, 1, 6, 4]
    # nums = [1, 3, 2, 2, 3, 1]
    # nums = [1, 1, 1, 2, 2, 2]
    # nums = [2,3,3,2,2,2,1,1]
    # nums =[1, 1, 2, 1, 2, 2, 1]
    nums = [4, 5, 5, 6]
    Sol().wiggle(nums)
    print(nums)
