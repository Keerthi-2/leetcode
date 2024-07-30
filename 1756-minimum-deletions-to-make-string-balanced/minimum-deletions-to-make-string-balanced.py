class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n=len(s)
        
        count_a=[0]*n
        count_b=[0]*n
        
        bc=0
        for i in range(n):
            count_b[i]=bc
            if s[i]=='b':
                bc+=1
        
        ac=0
        for i in range(n-1,-1,-1):
            count_a[i]=ac
            if s[i]=='a':
                ac+=1
        
        res=float('inf')
        
        for i in range(n):
            res=min(res,count_b[i]+count_a[i])
        
        return res
            