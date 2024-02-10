# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        l=[]
        temp=head

        while(temp):
            l.append(temp.val)
            temp=temp.next
        ans=[0]*len(l)
        st=[]
        for i in range(len(l)):
            while(len(st)>0 and l[st[-1]]<l[i]):
                cur=st.pop()
                ans[cur]=l[i]
            st.append(i)
        print(ans)
        
        return ans
        