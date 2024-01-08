# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:


        def inorder(root):
            
            if root is None:
                return 
            inorder(root.left)
            if low<=root.val<=high:
                self.ans+=root.val
            inorder(root.right)

        inorder(root)
        return self.ans
        