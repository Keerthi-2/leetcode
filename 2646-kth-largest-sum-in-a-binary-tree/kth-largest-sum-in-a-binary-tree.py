# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        ans=0
        q=[root]
        
        res=[]
        while(q):
            size=len(q)
            
            cur_sum=0
            print(k,cur_sum)
            for i in range(size):
                cur=q.pop(0)
                cur_sum+=cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            res.append(cur_sum)
        res.sort()
        print(res)
        if len(res)<k:
            return -1
        
        l=len(res)
        return res[l-k]
            