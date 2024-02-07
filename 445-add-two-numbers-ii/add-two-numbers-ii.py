# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=[]
        s2=[]
        dummy=None
        temp=dummy
        while(l1):
            s1.append(l1.val)
            l1=l1.next

        while(l2):
            s2.append(l2.val)
            l2=l2.next
        carry=0
        cur_sum=0
        while(len(s1) or len(s2)):
            cur_sum=0
            if len(s1)>0:
                cur_sum+=s1.pop()
            if len(s2)>0:
                cur_sum+=s2.pop()
            
            cur_s=cur_sum+carry
            carry=cur_s//10
            new=ListNode(cur_s%10)
            new.next=dummy
            dummy=new
        
        print(carry)
        if carry>0:
            new=ListNode(1)
            new.next=dummy
            dummy=new

            
        return dummy
            
        