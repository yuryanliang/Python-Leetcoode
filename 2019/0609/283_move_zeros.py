def moveZeroes(nums):
    y=0
    for x in range(len(nums)):
        if nums[x]!=0:
            nums[x],nums[y]=nums[y],nums[x]
            y+=1