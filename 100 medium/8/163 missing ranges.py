"""
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]

"""
class Sol:
    def range(self, nums):
        res = []
        if nums[0]==0:
            end = nums[0]
        else:
            if nums[0]==1:
               res.append("0")
               end = 1
            else:
                res.append("0->"+ str(nums[0]-1))
                end = nums[0]

        for i in range(1, len(nums)):

            if nums[i]==nums[i-1]+1:
                end = nums[i]
            else:
                end +=1
                start = nums[i]-1
                interval=str(end)

                if end != start:
                    interval+='->'+str(start)
                res.append(interval)
                end = nums[i]

        if end != 99:
            end +=1
            interval = str(end)
            if end !=99:
                interval+='->99'
            res.append(interval)
        return res
class Sol1:
    def range(self, nums, lower, upper):
        def get_range(start,end):
            if start == end:
                return str(start)
            else:
                return str(start)+"->"+str(end)
        res = []
        pre = lower -1

        for i in range(len(nums)+1):
            if i == len(nums):
                cur = upper +1
            else:
                cur = nums[i]

            if cur - pre >= 2:
                res.append(get_range(pre+1, cur-1))
            pre = cur
        return res

if __name__ == '__main__':
    nums=[0, 1, 3, 50, 75]
    nums= [3, 4, 5, 90]
    print(Sol1().range(nums, 0, 99))
