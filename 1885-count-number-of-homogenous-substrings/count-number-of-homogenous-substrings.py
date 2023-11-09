class Solution:
    def countHomogenous(self, s: str) -> int:
        
        res=0
        mod=10**9+7
        i=0
        while(i<len(s)):
            cur=s[i]
            j=i+1
            
            while(j<len(s) and cur==s[j]):
                j+=1
            
            res+=((j-i)*(j-i+1))//2
            res=res%mod
            i=j
        return res


        # a b b b   c d
        # 1+