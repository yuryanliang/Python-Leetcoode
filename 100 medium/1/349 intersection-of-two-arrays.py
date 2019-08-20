"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
# two pointer
class Sol1:
    def inter(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res=[]
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not (len(res) and nums1[i] == res[-1]):
                    res.append(nums1[i])
                i += 1
                j += 1
        return res

    def inter(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i , j = 0, 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j +=1
            else:
                if not (len(res) and nums1[i]==res[-1]):
                    res.append(nums1[i])
                i +=1
                j +=1
        return res





#brute force
class Sol2:
    def inter(self, nums1, nums2):
        res = []
        for i in nums2:
            if i in nums1 and i not in res:
                res.append(i)
        return res

    def inter(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res



# hast table
class Sol:
    def inter(self, nums1, nums2):
        lookup={}
        res = []
        for i in nums1:
            if i not in lookup:
                lookup[i] = 1
        for j in nums2:
            if j in lookup and j not in res:
                res.append(j)
        return res

    def inter(self, nums1, nums2):
        lookup ={}
        res = []
        for i in nums1:
            if i not in lookup:
                lookup[i] =1

        for j in nums2:
            if j in lookup and j not in res:
                res.append(j)
        return res

#hash table 2
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0

        return res



if __name__ == '__main__':
    # nums1 = [1,2,2,1]
    # nums2 = [2,2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Sol().inter(nums1, nums2))
