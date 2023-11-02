# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count=0
        def average(root):
            nonlocal count
            if root==None:
                return {"nodesum":0,"nodecount":0}
            
            dleft=average(root.left)
            dright=average(root.right)
            print(dleft,dright)
            nodesum=dleft["nodesum"]+dright["nodesum"]+root.val
            nodecount=dleft["nodecount"]+dright["nodecount"]+1
            avg=nodesum//nodecount
            if avg==root.val:
                count+=1

            return {"nodesum":nodesum,"nodecount":nodecount}

        average(root)
        return count
            

            
            

            
        