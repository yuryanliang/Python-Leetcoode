# Time:  O(n)
# Space: O(1)
#
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(0)
        tmp = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next= l1
                l1=l1.next
                tmp=tmp.next
            else:
                tmp.next = l2
                l2=l2.next
                tmp= tmp.next
        if l2 == None:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next

def merge2(test_list1, test_list2):

    size_1 = len(test_list1)
    size_2 = len(test_list2)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if test_list1[i] < test_list2[j]:
            res.append(test_list1[i])
            i += 1

        else:
            res.append(test_list2[j])
            j += 1

    return res + test_list1[i:] + test_list2[j:]