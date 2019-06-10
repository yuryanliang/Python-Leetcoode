class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(head):
    fast,slow=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next

        if fast is slow:
            return True
    return False
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print hasCycle(head)