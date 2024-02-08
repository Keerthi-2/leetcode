# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(h):
            l=0
            while(h):
                l+=1
                h=h.next
            return l
        if head is None or k==0 or head.next is None:
            return head
        fast=head
        l=length(head)
        if k==l or k%l==0:
            return head
        if k>l:
            k=k%l
        for i in range(1,k+1):
            if fast is None:
                return head
            fast=fast.next
        
        slow=head

        while(fast.next!=None):
            slow=slow.next
            fast=fast.next
        start=slow.next
        slow.next=None
        fast.next=head

        return start


        