# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tempA=headA
        tempB=headB

        while(tempA != tempB):
            tempA = tempA.next
            tempB = tempB.next
            if(tempA==tempB):
                return tempA
            if(tempA is None):
                tempA=headB
            if(tempB is None):
                tempB=headA
        
        return tempA
            

        



