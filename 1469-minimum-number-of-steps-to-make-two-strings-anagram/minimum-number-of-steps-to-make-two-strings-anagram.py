class Solution:
    def minSteps(self, s: str, t: str) -> int:

        count_t=[0]*26
        count_s=[0]*26

        for i in s:
            count_s[ord(i)-97]+=1
        
        for i in t:
            count_s[ord(i)-97]-=1
        
        ans=0
        for i in range(26):
            ans+=max(0,count_s[i])
        
        return ans


        