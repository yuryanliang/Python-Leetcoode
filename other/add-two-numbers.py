# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        

        idx = ListNode(0);       # 链表问题
        add = idx;
        ran = 0;
    
        while l1 or l2 or ran:
            v1 = 0;
            v2 = 0;
            if l1:
                v1 = l1.val;
                l1 = l1.next     # l1 从 l1 的 next 开始
            if l2:
                v2 = l2.val;
                l2 = l2.next
            
            add.next = ListNode((v1+v2+ran)%10);
            add = add.next;
            ran = (v1+v2+ran)/10;
           
            
        return idx.next

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
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        flag = 0
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            sum= l1.val + l2.val + flag
            curr.next = ListNode(sum % 10)
            flag = sum / 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        
        while l1:
            sum = l1.val + flag
            curr.next = ListNode (sum % 10)
            flag = sum / 10
            l1 = l1.next
            curr = curr.next
            
        while l2:
            sum = l2.val + flag
            curr.next = ListNode (sum % 10)
            flag = sum / 10
            l2 = l2.next
            curr = curr.next
        
        if flag == 1:
            curr.next = ListNode(1)
        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
