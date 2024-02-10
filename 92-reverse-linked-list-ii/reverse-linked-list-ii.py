# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev=head
        slow=head
        end=head
        prev_left=left
        prev_right=right
        if left==right:
            return head
        
        while(left!=1):
            prev=slow
            slow=slow.next
            left-=1

        while(right!=1):
            prev1=end
            end=end.next
            right-=1
        first_start=slow
        second_nex=end.next
        end.next=None
        prev_one=None
        while(slow!=None):
            next_one=slow.next
            slow.next=prev_one
            prev_one=slow
            slow=next_one
        prev.next=prev_one
        first_start.next=second_nex

        if prev_left==1 and prev_right!=1:
            head=end
        return head



        return head


        
        