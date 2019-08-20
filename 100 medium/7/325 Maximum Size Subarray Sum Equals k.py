"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""

class Sol1:
    def length(self, nums, k):
        max_length=0
        path=[]
        index=0
        self.helper(nums, max_length, path,index, k)
        return max_length

    def helper(self, nums, max_length, path, index,k):
        if sum(path) == k:
            max_length = max(max_length, len(path))
        else:
            for i in range(index,len(nums)):
                path.append(nums[i])
                self.helper(nums, max_length, path, index+1,k)
                path.pop(nums[i])

class Sol:
    def length(self, nums,k):
        sums={}
        cur_sum, max_len=0,0
        for i in range(len(nums)):
            cur_sum +=nums[i]
            temp=cur_sum -k
            if cur_sum ==k:
                max_len = i +1
            # i, j
            # sum[j] - sum[i] = k.
            # sum[j] - k = sum[i]
            elif cur_sum - k in sums:
                temp1 = i - sums[cur_sum - k]

                max_len=max(max_len, i- sums[cur_sum-k])
            if cur_sum not in sums:
                sums[cur_sum]=i
        return max_len



if __name__ == '__main__':
    nums=[-2, -1, 2, 1]
    k = 1
    print(Sol().length(nums, k))