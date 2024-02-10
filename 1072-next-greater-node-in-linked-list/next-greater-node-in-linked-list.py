# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        temp=head
        ans=[]
        st=[]
        ind=0
        while(temp):
            ans.append(0)
            while(len(st)>0 and temp.val>st[-1][1]):
                print(st)
                index,cur=st.pop()
                ans[index]=temp.val

            st.append((ind,temp.val))
            ind+=1

            temp=temp.next
       
        
        
        return ans
        