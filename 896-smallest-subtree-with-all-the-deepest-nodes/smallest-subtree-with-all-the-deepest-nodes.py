# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
  # l  root r     root l r
class Solution:
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        d={None:-1}
        max_depth=-1
        def dfs(root,parent=None):
            if root is None:
                return 
            d[root]=d[parent]+1
            dfs(root.left,root)
            dfs(root.right,root)
        dfs(root)

        for i in d:
            max_depth=max(max_depth,d[i])
        print(d,max_depth)
        def result(root):
            
            if root is None:
                return None
            if d[root]==max_depth:
                return root
            l=result(root.left)
            r=result(root.right)

            if l is not None and r is not None:
                return root
            if l is None:
                return r
            if r is None:
                return l
            
            return root
        
        return result(root)