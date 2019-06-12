def removeElement(nums, val):
    last = 0
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[last] = nums[i]
            last += 1
        i += 1
    return last


def removeElement2(nums, val):
    last = len(nums) - 1
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums[i], nums[last] = nums[last], nums[i]
            last -= 1
        else:
            i += 1
    return last + 1
