class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        d={}
        
        start=0
        end=0
        ans=0
        # bruet force: 0(n*n) n is length of string
        n=len(s)
        
        while(end<n):   # abcabcbb   start=0 end=0  {a:1}
            #  end=1 {a:1,b:1} end=2  {a:1,b:1,c:1}   end=3 {a:2,b:1,c:1} {a:1,b:1,c:1} start=1
            
            if s[end] in d and d[s[end]]>=start:
                start=d[s[end]]+1
                
            d[s[end]]=end
            ans=max(ans,end-start+1)
            end+=1
        
        
        
        return ans
            
            
        
        