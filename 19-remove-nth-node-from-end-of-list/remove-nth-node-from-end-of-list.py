# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head

        for i in range(1,n+1):
            fast=fast.next
        if fast is None:
            return head.next
        while(fast!=None):
            prev=slow
            slow=slow.next
            fast=fast.next
        print(slow.val)
        prev.next=slow.next
        return head
        