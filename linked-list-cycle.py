# Time:  O(n)
# Space: O(1)
#
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?
#

'''解题思路：
题目可以在O(n)时间复杂度内求解

算法步骤：

使用两个"指针"x和y，初始令y = 0

利用x遍历数组nums：

若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

算法简析：

y指针指向首个0元素可能存在的位置

遍历过程中，算法确保[y, x)范围内的元素均为0'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                return True
        return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().hasCycle(head)
