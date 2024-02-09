# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head=less_tail=ListNode(0)
        great_head=great_tail=ListNode(0)

        while(head!=None):
            if head.val<x:
                less_tail.next=head
                less_tail=less_tail.next
            else:
                great_tail.next=head
                great_tail=great_tail.next
            
            head=head.next
        great_tail.next=None
        less_tail.next=great_head.next
        return less_head.next

        