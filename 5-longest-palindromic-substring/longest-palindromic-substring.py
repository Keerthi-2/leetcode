class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        ans=0
        
        l=0
        start=0
        r=0
        n=len(s)
        for i in range(n):
            
            l,r=i,i+1
            
            while(l>=0 and r<n and s[l]==s[r]):
                if r-l+1>ans:
                    ans=r-l+1
                    start=l
                
                l-=1
                r+=1
                
                
            l,r=i,i
            
            while(l>=0 and r<n and s[l]==s[r]):
                if r-l+1>ans:
                    ans=r-l+1
                    start=l
                l-=1
                r+=1  
                
            print(start,ans)
        
        return s[start:start+ans]