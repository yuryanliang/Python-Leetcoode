题目原文
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
1
2
3
4
5
begin to intersect at node c1.

Notes: 
1. If the two linked lists have no intersection at all, return null. 
2. The linked lists must retain their original structure after the function returns. 
3. You may assume there are no cycles anywhere in the entire linked structure. 
4. Your code should preferably run in O(n) time and use only O(1) memory.

题目翻译
写一个程序，找到两个单链表交汇的节点。比如，下面两个单链表交汇节点是c1：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
1
2
3
4
5
注意：1，如果两个单链表不交，返回null；2，函数返回后，两个单链表的原始顺序不能改变；3，假定整个结构中没有环；4，你的程序最好以时间复杂度O(n)，空间复杂O(1)运行。

思路方法
思路一
假设两个链表有交叉，那么交叉后的长度是一样的，而交叉前的长度可能不一致。如果我们将两个链表的交叉前的长度截成一致，那么就可以同时遍历两个链表，判断是否有相交节点。截断交叉前的不同长度等价于截断两个完整链表的不同长度。此方法需要计算两个链表长度。

代码

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def getListLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
思路二
事实上，可以不用计算两个链表的长度，因为本质上我们关心的是让两个链表的指针同时到达交叉点。我们可以定义两个指针，让它们都将两个链表都遍历一遍，那么它们走的总长度是一样的，倘若两个链表相交，那么这两个指针一定会在某个地方相等。

代码

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p and q and p != q:
            p = p.next
            q = q.next
            if p == q:
                return p
            if not p:
                p = headB
            if not q:
                q = headA
        return p
