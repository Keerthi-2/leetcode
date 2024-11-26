class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        res=[0]*n
        
        for u,v in edges:
            
            res[v]+=1
        
        count=0
        ans=0
        
        for i in range(n):
            if res[i]==0:
                count+=1
                ans=i
        
        
        if count>1:
            return -1
        
        
        return ans