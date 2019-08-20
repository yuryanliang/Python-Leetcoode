"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""
"""
找最后一个单调递减区间，
区间的前一个点就是 pivot 
把pivot 和 最后面数起， 第一个大于pivot的值交换
把原单调递减区间sort

edge case：
找不到pivot 原函数递减，return 直接reverse

"""

class Sol:
    def next(self, nums):
        piv = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                piv = i
        if piv == -1:
            nums.reverse()
            return

        small = 0
        for i in range(piv + 1, len(nums)):
            if nums[i] > nums[piv]:
                small = i

        nums[piv], nums[small] = nums[small], nums[piv]
        nums[piv + 1:] = sorted(nums[piv + 1:])
        return nums

    def next(self, nums):
        piv = -1
        for i in range(len(nums) -1):
            if nums[i] > nums[i + 1]:
                piv = i
        if piv == -1:
            nums.reverse()
            return

        small = 0

        for i in range(piv + 1, len(nums)):
            if nums[i]< nums[piv]:
                small = i

        nums[piv], nums[small] = nums[small], nums[piv]

        nums[piv + 1:] = sorted(nums[piv+1 :])

        return nums

def main():
    nums = [1, 3, 2]
    # nums = [1, 1, 5]
    print(Sol().next(nums))


if __name__ == '__main__':
    main()
