# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        prev=slow
        slow=slow.next
        prev.next=None

        while(slow):
            nex=slow.next
            slow.next=prev
            prev=slow
            slow=nex
        last=prev
        first=head

        while(first):
            
            if first is None or last is None:
                break
            if first.val!=last.val:
                return False
            first=first.next
            last=last.next
        return True

        
        