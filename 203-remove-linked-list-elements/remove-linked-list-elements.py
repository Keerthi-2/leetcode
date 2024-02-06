# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        prev=None
        temp=head
        flag=False
        while(temp!=None):
            print(temp.val)
            
            while temp is not None and temp.val==val:
                if flag is False:
                    flag=True
                temp=temp.next
            if prev==None:  
                if flag:
                    head=temp
            else:
                if prev.next!=temp:
                    prev.next=temp
            if temp is None:
                return head
            prev=temp
            temp=temp.next
        return head
            


        