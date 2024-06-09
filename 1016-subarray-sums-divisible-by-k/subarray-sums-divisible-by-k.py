class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        d={}
        pf=0
        ans=0
        
        for i in range(len(nums)):
            pf+=nums[i]
            pf=pf%k
            
            if pf in d:
                ans+=d[pf]
                d[pf]+=1
            else:
                d[pf]=1
            
            if pf==0:
                ans+=1
        
        return ans