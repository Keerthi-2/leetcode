# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow=head
        fast=head
        while fast and (fast.next):
            slow=slow.next
            fast=fast.next.next
        current=slow
        prev=None
        while current!=None:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        while prev.next:
            nxt=head.next
            head.next=prev
            head=nxt
            
            nxt=prev.next
            prev.next=head
            prev=nxt
            
        