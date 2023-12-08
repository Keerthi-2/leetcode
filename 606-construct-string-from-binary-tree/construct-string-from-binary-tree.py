# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
      
      def dfs(root):
        if root is None:
          return
        res.append(str(root.val))
        if root.left is None and root.right is None:
          return
        
        res.append('(')
        dfs(root.left)
        res.append(')')

        if root.right:
          res.append('(')
          dfs(root.right)
          res.append(')')

      res=[]
      dfs(root)

      return ''.join(res)
        