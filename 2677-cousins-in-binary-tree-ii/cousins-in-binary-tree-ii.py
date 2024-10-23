# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        level_sum=[]
        
        q=[root]
        while(q):
            l=len(q)
            level=0
            
            for _ in range(l):
                cur=q.pop(0)
                level+=cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            level_sum.append(level)
        
        print(level_sum,l)
        q1=[root]
        level_index=1
        root.val=0
        
        
        while(q1):
            level_size=len(q1)
            print(level_index)
            for _ in range(level_size):
                cur=q1.pop(0)
                
                siblings=(cur.left.val if cur.left else 0)+(cur.right.val if cur.right else 0)
                if cur.left:
                    cur.left.val=(level_sum[level_index]-siblings)
                    q1.append(cur.left)
                    
                if cur.right:
                    cur.right.val=(level_sum[level_index]-siblings)
                    q1.append(cur.right)
                    
            level_index+=1
        
        return root