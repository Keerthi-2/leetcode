# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos=2
        prev=head
        prev_critical_index=0
        cur_critical_index=0
        cur=head.next
        min_dis=float('inf')
        max_dis=-1
        while(cur.next!=None):
            
            if (prev.val<cur.val and cur.next.val<cur.val)  or (prev.val>cur.val and cur.next.val>cur.val):
                print(cur.val,pos)
                if prev_critical_index==0:
                    print("pos is", pos)
                    prev_critical_index=pos
                    cur_critical_index=pos
                else:
                    min_dis=min(min_dis,pos-cur_critical_index)
                    cur_critical_index=pos
            pos+=1
            prev=cur
            cur=cur.next
        
        print(prev_critical_index,cur_critical_index,min_dis)
        if min_dis!=float('inf'):
            max_dis=max(max_dis,cur_critical_index-prev_critical_index)
        else:
            min_dis=-1
        return [min_dis,max_dis]





            

        