# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        sum1 = 0
        hm = {}
        prev = None

        while(current ):
            sum1 += current.val 
            if sum1 == 0 :
                if current.next :
                    head = current.next
                    hm = {}
                else : 
                    return
            elif sum1 not in hm : 
                hm[sum1] = current
            else :
                prev = hm[sum1]
                start_removal_node = prev.next
                while start_removal_node != current :
                    sum1 = sum1 + start_removal_node.val
                    hm.pop(sum1)
                    start_removal_node = start_removal_node.next
                prev.next = current.next
                sum1 += current.val 
            current = current.next
        
        return head