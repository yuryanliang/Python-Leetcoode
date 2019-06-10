class TwoSum:
    def __init__(self):
        self.nums={}
    def add(self, number):
        if number in self.nums:
            self.nums[number]+=1
        else:
            self.nums[number]=1

    def find(self,value):
        nums=self.nums
        for n in nums:
            if value - n in nums and (value-n!=n or nums[n]>=2):
                return True
        return False
