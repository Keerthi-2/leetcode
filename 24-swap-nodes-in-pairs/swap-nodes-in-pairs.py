# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next is None:
            return head
        def recursion(cur):
            if cur==None or  cur.next==None:
                return cur

            end=cur.next
            nex=end.next
            end.next=cur

            cur.next=recursion(nex)
            return end


        return recursion(head)
        