# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        d={}
        def inorder(root):
            if root==None:
                return 
            inorder(root.left)
            if root.val not in d:
                d[root.val]=1
            else:
                d[root.val]+=1
            inorder(root.right)
        inorder(root)
        
        max_val=0
        for val in d.values():
            max_val=max(max_val,val)
        
        ans=[]
        for k,v in d.items():
            if v==max_val:
                ans.append(k)
        
        return ans
        


        