class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans=-1
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for i in range(len(s)):
            if d[s[i]]==1:
                ans=i
                break
        
        return ans