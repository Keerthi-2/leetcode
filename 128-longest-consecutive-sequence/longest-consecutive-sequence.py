class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
       
        for i in s:
            prev=i-1
           
            res=1
            cur=i+1
            if prev not in s:
                while(cur in s):
                    cur+=1
                    res+=1
            
                ans=max(ans,res)
        
        return ans