# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=[]
        temp=head
        while(head!=None):
            s.append(head.val)
            head=head.next
        new=None
        ans=new
        carry=0
        while(len(s)):
            if len(s)>0:
                cur=s.pop()
            cur=cur*2+carry
            print(carry,cur%10)
            new_node=ListNode(cur%10)
            carry=cur//10
            new_node.next=new
            new=new_node
        if carry==1:
            new_node=ListNode(1)
            new_node.next=new
            new=new_node
        return new
        
        

        return new

        