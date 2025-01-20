class Solution:
    def deleteNode(self, A: Optional[TreeNode], B: int) -> Optional[TreeNode]:
        if(A):
            if(B < A.val): 
                A.left = self.deleteNode(A.left, B)                 
            elif(B > A.val): 
                A.right = self.deleteNode(A.right, B)       
            else:
                if(not A.left and not A.right): 
                    return None             
                if (not A.left or not A.right):
                    return A.left if A.left else A.right           
                                                                  
                temp = A.left                         
                while(temp.right != None): 
                    temp = temp.right 

                temp.right=A.right
                head= A.left
                A.left=None
                return head
                # A.val = temp.val                     
                # A.left = self.solve(A.left, temp.val)
            
        return A;
