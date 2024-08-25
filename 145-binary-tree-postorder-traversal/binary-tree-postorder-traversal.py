# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[root]
        if root is None:
            return []
        res=[]
        while(len(st)):
            cur=st.pop()
            res.insert(0,cur.val)
            
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)
        
        return res
        