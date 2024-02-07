# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while(fast!=None):
            first_end=slow
            slow=slow.next
            fast=fast.next.next
        
        cur=slow
        prev=None
        while(cur!=None):
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        first_end.next=prev
        ans=0
        while(prev!=None):
            ans=max(ans,prev.val+head.val)
            head=head.next
            prev=prev.next
            

        return ans

        