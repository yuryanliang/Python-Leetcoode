"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
用指针 每一位移动
计算carry
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print ("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))

class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def add_two(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2:
            new_sum = int()
            if l1 and l2:
                new_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                new_sum = l2.val + carry
                l2 = l2.next
            elif not l2:
                new_sum = l1.val + carry
                l1 = l1.next

            if new_sum < 10:
                cur.next = ListNode(new_sum)
                carry = 0
            else:
                cur.next = ListNode(new_sum % 10)
                carry = 1
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return dummy.next

    def add_two(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        carry = 0

        while l1 or l2:
            new_sum = int()
            new_sum += carry
            if l1:
                new_sum += l1.val
                l1 = l1.next
            if l2:
                new_sum += l2.val
                l2 = l2.next

            if new_sum < 10:
                cur.next = ListNode(new_sum)
                carry = 0
            else:
                cur.next = ListNode(new_sum % 10)
                carry = 1
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return dummy.next

