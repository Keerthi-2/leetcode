# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        ans=[]
        inorder(root)
        def sortedtobst(s,e):
            if s>e:
                return None
            m=(s+e)//2
            root=TreeNode(ans[m])
            root.left=sortedtobst(s,m-1)
            root.right=sortedtobst(m+1,e)
            return root
            
        return sortedtobst(0,len(ans)-1)
