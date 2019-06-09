def removeElement(self, nums, val):
    last=0
    i=0
    while i <len(nums):
        if nums[i]!=val:
            nums[last]=nums[i]
            last+=1
        i+=1
    return last