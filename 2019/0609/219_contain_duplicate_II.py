def containsNearbyDuplicate(nums, k):
    num_map={}
    for i in xrange(len(nums)):
        if nums[i] in num_map and i-num_map[nums[i]]<=k:
            return True
        else:
            num_map[nums[i]]=i
    return False