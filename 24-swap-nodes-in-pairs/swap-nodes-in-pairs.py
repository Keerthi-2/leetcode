# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode(0)
        s.next = head
        l = s
        while l.next and l.next.next :
            rr = l.next.next
            l.next.next = l.next.next.next
            rr.next = l.next
            l.next = rr
            l = l.next.next
        return s.next     