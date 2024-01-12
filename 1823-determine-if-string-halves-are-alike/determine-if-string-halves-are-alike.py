class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v=['a','e','i','o','u','A','E','I','O','U']
        lcount=0
        rcount=0
        l=0
        r=len(s)-1
        while(l<r):
            if s[l] in v:
                lcount+=1
            if s[r] in v:
                rcount+=1
            l+=1
            r-=1
        


        
        return lcount==rcount
        