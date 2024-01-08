# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:


        def inorder(root):
            
            if root is None:
                return 0
            current=0
            if low<=root.val<=high:
                current=root.val
            l=inorder(root.left)
            
            r=inorder(root.right)
            return current+l+r

        return inorder(root)
      
        