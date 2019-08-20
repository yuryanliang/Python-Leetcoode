"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
backtracking

因为没有重复的数， 所以在加入alist 之前可以判断一下是不是 这个数已经取过。
"""

class Sol:
    def permute(self, nums):

        result = []
        alist = [] #代表已取出的数

        self.helper(nums, alist, result)
        return result

    def helper(self, nums, alist, res):
        if len(alist) == len(nums):
            # temp = alist.copy()  # append a copy of alist
            res.append(list(alist)) # (alist[:])
            return

        for i, item in enumerate(nums):
            if item not in alist: #取过的数不再取
                alist.append(item)
                self.helper(nums, alist, res)
                 #重要！！遍历过此节点后，
                # 要回溯到上一步，因此要把加入到结果中的此点去除掉！
                alist.pop()


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRecu(result, used, [], num)
        return result

    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur[:])
            return
        for i in range(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False
def main():
    nums = [1, 2, 3]
    print(Sol().permute(nums))


if __name__ == '__main__':
    main()


