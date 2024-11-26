class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        res=[0]*n
        
        for u,v in edges:
            
            res[v]+=1
        
        count=0
        ans=-1
        
        for i in range(n):
            if res[i]==0:
                if ans!=-1:
                    return -1
                ans=i
        
        
        
        
        
        return ans