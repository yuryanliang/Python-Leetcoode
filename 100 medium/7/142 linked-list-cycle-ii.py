"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.




Follow-up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head.next
            fast = head.next.next
            while  fast is not slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def det(self, head):
        try:  ##如果有尾部，必然出错，进入except。
            Slow = head.next  ## 保证Slow和 Fast同时移动
            Fast = head.next.next
            while Slow != Fast:  ## Fast一直是Slow的两倍速度，这点很关键。
                Slow = Slow.next
                Fast = Fast.next.next
        except:
            return None
        Slow = head  ##让Slow从头开始，Fast保持上一步的位置
        while Slow != Fast:
            Slow = Slow.next
            Fast = Fast.next
        return Slow


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    print(Solution().detectCycle(head))
