class Solution:
    def deleteNode(self, A: Optional[TreeNode], B: int) -> Optional[TreeNode]:
        if not A:
            return A
        
        parent=None
        cur=A
        
        while(cur and cur.val!=B):
            parent=cur
            if B<cur.val:
                cur=cur.left
            elif B>cur.val:
                cur=cur.right

        if cur is None:
            return A       
        #print(cur.val)
        if cur.left is None and cur.right is None:
            #print("no child")
            if parent is None:
                #print("oh")
                return None
                
            if parent.left==cur:
                parent.left=None
            else:
                parent.right=None
                
        
        elif cur.left is None or cur.right is None:
            #print("one child")
            child=None
            if cur.left:
                child=cur.left
            else:
                child=cur.right
            
            if parent is None:
                return child
            
            if parent.left==cur:
                parent.left=child
            else:
                parent.right=child
                
        else:
          #  print("two child")
            left_node=cur.left
            prev_pred=None
            while(left_node.right is not None):
                prev_pred=left_node
                left_node=left_node.right
                
            cur.val=left_node.val
            
            if prev_pred is None:
                cur.left=left_node.left
            else:
                prev_pred.right=left_node.left
                
        
        return A
