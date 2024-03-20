# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a=a-1
        b=b+1

        cur=list1
        while(a>0):
            cur=cur.next
            a-=1
        
        end=list1
        while(b>0):
            end=end.next
            b-=1
        cur.next=list2
        new=list2
        while(list2.next!=None):
            list2=list2.next
        list2.next=end

        return list1