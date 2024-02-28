# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        q=[root]
        cur=root
        while(len(q)):
            cur=q.pop(0)
                
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        
        print(cur.val)
        return cur.val
        