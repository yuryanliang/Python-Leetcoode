# brute force

"""
input structure
[]
sorted
repeated
neg
one sol, guarantee

output
index, number
False, -1, 
"""


class TwoSum:
    def two_sum(self, nums, target):
        # []
        if len(nums) < 2:
            return -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return -1


def main():
    nums = [4, 2, 1]
    target = 6
    print(TwoSum().two_sum(nums, target))


# 2 pointer
class TwoSum_2:
    def two_sum(self, nums, target):

        l = sorted(nums)
        left = 0
        right = len(l) - 1

        while left < right:
            if l[left] + l[right] == target:
                if l[left] == l[right]:
                    i_1 = nums.index(l[left])
                    import sys  # [0, 4, 6, 0] for 0. [3, 3] for 6
                    nums[i_1] = sys.maxsize
                    i_2 = nums.index(l[right])
                    return [i_1, i_2]

                i_1 = nums.index(l[left])
                i_2 = nums.index(l[right])

                return [i_1, i_2] if i_1 < i_2 else [i_2, i_1] # swap i to make the smaller go first
            elif l[left] + l[right] < target:
                left += 1
            else:
                right -= 1

def main_2():
    nums = [4, 2, 1]
    target = 6
    print(TwoSum_2().two_sum(nums, target))


# hash table
class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup.get(target - nums[i]), i]
            else:
                lookup[nums[i]] = i


class TwoSum_3:
    def two_sum(self, nums, target):
        lookup = {}
        for i, val in enumerate(nums):
            if target - val in lookup:
                return [lookup.get(target - val), i]
            else:
                lookup[val] = i
        return -1

def main_3():
    nums = [4, 2, 1]
    target = 5
    print(TwoSum_2().two_sum(nums, target))

if __name__ == "__main__":
    main_3()

