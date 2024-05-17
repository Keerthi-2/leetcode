# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        
        def leafnode(cur):
            if cur.left is None and cur.right is None and cur.val==target:
                return True
            return False
        if leafnode(root):
            return None
        
        def dfs(node):
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if leafnode(node):
                return None
            
            return node
                    
                
        
        
        return dfs(root)
        