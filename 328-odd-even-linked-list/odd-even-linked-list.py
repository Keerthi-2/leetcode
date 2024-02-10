# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_tail=ListNode(-1)
        odd_head=odd_tail
        even_tail=ListNode(-1)
        even_head=even_tail

        cur=head
        f=True
        while(cur):
            if f:
                odd_tail.next=cur
                odd_tail=odd_tail.next
                f=False
            else:
                even_tail.next=cur
                even_tail=even_tail.next
                f=True
            cur=cur.next
        odd_tail.next=even_head.next
        even_tail.next=None

        return head
            