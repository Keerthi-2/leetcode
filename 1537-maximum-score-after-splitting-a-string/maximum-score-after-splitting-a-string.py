class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        pf=[0]*n

        if s[n-1]=="1":
            pf[n-1]=1
        for i in range(n-2,-1,-1):
            if s[i]=="1":
                pf[i]=pf[i+1]+1
            else:
                pf[i]=pf[i+1]

        ans=0
        zero=0
        for i in range(n-1):
            if s[i]=="0":
                zero+=1
            ans=max(ans,pf[i+1]+zero)
        
        return ans