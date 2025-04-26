# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur=head
        count=0

        while(cur and count<k):
            cur=cur.next
            count+=1
        if(count<k):
            return head
        
        newhead=None
        curnode=head
        while(curnode is not cur):
            temp=curnode
            curnode=curnode.next
            temp.next=newhead
            newhead=temp
        
        head.next=self.reverseKGroup(cur,k)

        return newhead
        


        