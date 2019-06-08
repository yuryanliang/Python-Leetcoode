def rotate(nums, k):
    k %= len(nums)
    reverse(nums, 0, len(nums) )
    reverse(nums, 0, k)
    reverse(nums, k, len(nums) )


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end-1] = nums[end-1], nums[start]
        start += 1
        end -= 1
nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums,3)
print nums