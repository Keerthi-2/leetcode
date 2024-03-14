class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur=0
        ans=0
        d={}
        for  i in range(len(nums)):
            cur+=nums[i]
            if cur==goal:
                ans+=1
            
            if cur-goal in d:
                ans+=d[cur-goal]
            
            if cur in d:
                d[cur]+=1
            else:
                d[cur]=1
        
        return ans
        