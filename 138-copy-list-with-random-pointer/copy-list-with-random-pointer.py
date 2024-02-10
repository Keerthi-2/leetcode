"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None
        temp=head
        while(temp):
            new_node=Node(temp.val,temp.next)
            temp.next=new_node
            temp=new_node.next
        
        temp=head
        while(temp):
            random_node=temp.random
            if random_node!=None:
                temp.next.random=random_node.next
            temp=temp.next.next

        ref=head.next
        ans=ref
        temp=head
        while(ref.next):
            temp.next=temp.next.next
            temp=temp.next
            ref.next=ref.next.next
            ref=ref.next
            

        return ans