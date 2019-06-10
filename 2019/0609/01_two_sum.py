def twoSum(nums, target):
    for i in xrange(len(nums)-1):
        for j in xrange(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]

def twoSum2(nums,target):
    keys={}
    for i in xrange(len(nums)):
        if target-nums[i] in keys:
            return [keys[target-nums[i]], i]
        if nums[i] not in keys:
            keys[nums[i]]=i