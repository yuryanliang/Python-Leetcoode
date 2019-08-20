"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Sol:
    def swap(self,head):
        if head is None or head.next is None: # 终止条件
            return head

        rev_rest = self.swap(head.next.next) # 1:head-> 2:node2 -> None;
        node2 = head.next
        node2.next = head
        head.next = rev_rest
        return node2



class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            node1, node2, node3 = cur.next, cur.next.next, cur.next.next.next
            cur.next = node2
            node2.next = node1
            node1.next = node3
            cur = cur.next.next

        return dummy.next



if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    # print(Solution().swapPairs(head))
    print(Sol().swap(head))


