class Solution:
    def longestPalindrome(self, S: str) -> str:
        resl=0
        start=0
        for i in range(len(S)):
            l,r=i,i
            while(l>=0 and r<len(S) and S[l]==S[r]):
                if r-l+1>resl:
                    resl=r-l+1
                    start=l
                    
                l-=1
                r+=1
            l,r=i,i+1
            while(l>=0 and r<len(S) and S[l]==S[r]):
                if r-l+1>resl:
                    resl=r-l+1
                    start=l
                l-=1
                r+=1
        return S[start:start+resl]
        