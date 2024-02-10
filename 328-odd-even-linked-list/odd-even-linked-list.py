# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        e=head.next
        o=head
        even_start=e
        while(e and e.next):
            o.next=e.next
            e.next=e.next.next

            o=o.next
            e=e.next
        
        o.next=even_start
        return head
