# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,d):
            if root is None:
                return 
            if d>self.depth:
                self.ans=root.val
                self.depth=d
            dfs(root.left,d+1)
            dfs(root.right,d+1)
        self.ans=0
        self.depth=-2
        dfs(root,0)

        return self.ans
        