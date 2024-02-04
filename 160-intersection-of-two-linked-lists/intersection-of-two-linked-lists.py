# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):

            l=0
            while(head!=None):
                l+=1
                head=head.next
            return l

        l1=length(headA)
        l2=length(headB)
        first=headA
        second=headB
        if l1<l2:
            first=headB
            second=headA
        d=abs(l1-l2)
        print(d)
        temp=first
        while(d!=0):
            
            first=first.next
            d-=1
        while(first!=second):
            first=first.next
            second=second.next
        return first
            

