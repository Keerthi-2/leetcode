# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        connector = None
        curr = head
        group_count = 1
        count = 1

        def reverse_between(pre, n):
            start = pre.next
            then = start.next
            after = start

            for _ in range(n - 1):
                start.next = then.next
                then.next = pre.next
                pre.next = then
                then = start.next

            return after

        while curr:
            if group_count == count or not curr.next:
                if count % 2 == 0:
                    curr = reverse_between(connector, count)
                connector = curr
                group_count += 1
                count = 0

            count += 1
            curr = curr.next

        return head