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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=[]
        temp=head
        while(temp!=None):
            s.append(temp.val)
            temp=temp.next
        new=None
        
        carry=0
        while(len(s) or carry==1):
            if len(s)>0:
                cur=s.pop()
            
            cur=cur*2+carry
            print(carry,cur%10)
            new_node=ListNode(cur%10)
            carry=cur//10
            new_node.next=new
            new=new_node
            cur=0
        
        return new
        
        

        

        

        