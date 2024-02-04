# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp=head
        if(temp is None):
            return temp
        while(temp!=None and temp.next!=None):
            if(temp.val==temp.next.val):
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
        