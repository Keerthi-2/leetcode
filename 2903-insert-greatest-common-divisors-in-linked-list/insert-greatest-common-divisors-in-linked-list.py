# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        def gcd(x,y):
            if y==0:
                return x
            return gcd(y,x%y)
        slow=head
        fast=head.next
        while(fast!=None):
            print(slow.val,fast.val)
            if slow.val>fast.val:
                x=slow.val
                y=fast.val
            else:
                x=fast.val
                y=slow.val
            cur=gcd(x,y)
            

            new_node=ListNode(cur)
            
            slow.next=new_node
            new_node.next=fast
            slow=fast
            fast=slow.next
        
        return head

        