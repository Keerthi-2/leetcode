# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        q=[root]
        f=1
        while(q):
            l=len(q)
            if f==1:
                prev=-1
                for i in range(l):
                    cur=q.pop(0)
                    if cur.val<=prev or cur.val%2==0:
                        print("odd",cur.val)
                        return False
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    prev=cur.val
            else:
                
                prev=10**8
                for i in range(l):
                    cur=q.pop(0)
                    if cur.val>=prev or cur.val%2!=0:
                        print("even",cur.val,prev)
                        return False
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    prev=cur.val
            if f==1:
                f=0
            else:
                f=1
        
        return True
            

