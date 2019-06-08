def majority_element(nums):
    nums_set=set(nums)
    for i in nums_set:
        if nums.count(i)>len(nums)/2:
            return i