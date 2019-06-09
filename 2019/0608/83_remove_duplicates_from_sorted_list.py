class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

def deleteDuplicates(self, head):
    cur=head
    while cur:
        runner=cur.next
        while runner and runner.val==cur.val:
            runner=runner.next
        cur.next=runner
        cur=runner
    return head