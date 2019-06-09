def getInterSectionNode(headA, headB):
    curr_list = set()
    while (headA):
        curr_list.add(headA)
        headA = headA.next

    while (headB):
        if headB in curr_list:
            return headB
        headB = headB.next
    return None
