# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur=head
        nex=head.next
        new=ListNode(0)
        ans=new
        if head is None:
            return head
        temp=0
        while(nex):
            
            if nex.val!=0:
                temp+=nex.val
                
            if nex.val==0:
                new_node=ListNode(temp)
                new.next=new_node
                new=new.next
                temp=0
            
            nex=nex.next
        return ans.next



