class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def reverseList(head):
    if head is None:
        return head
    new_head=head
    while head.next is not None:
        current =head.next
        head.next=head.next.next
        current.next = new_head
        new_head=current
    return new_head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print reverseList(head)