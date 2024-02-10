# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        mat=[[-1 for i in range(n)]for j in range(m)]
        if head is None:
            return mat
        top=0
        bottom=m-1
        left=0
        right=n-1
        cur=head
        
        while(cur):
            for c in range(left,right+1):
                if cur!=None:
                    
                    mat[top][c]=cur.val
                    cur=cur.next
                else:
                    break
            top+=1
            

            for r in range(top,bottom+1):
                if cur!=None:
                    mat[r][right]=cur.val
                    cur=cur.next
                else:
                    break
            
            right-=1
            
            if top<=bottom:
                for c in range(right,left-1,-1):
                    if cur!=None:
                        mat[bottom][c]=cur.val
                        cur=cur.next
                    else:
                        break
               
                bottom-=1

            if left<=right:
                for r in range(bottom,top-1,-1):
                    if cur!=None:
                        mat[r][left]=cur.val
                        cur=cur.next
                    else:
                        break
                
                left+=1
        return mat
        