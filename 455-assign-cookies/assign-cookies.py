class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cur_g=0
        cur_s=0
        ans=0
        while(cur_g<len(g) and cur_s<len(s)):
            if s[cur_s]>=g[cur_g]:
                ans+=1
                cur_g+=1
            cur_s+=1
        
        return ans
