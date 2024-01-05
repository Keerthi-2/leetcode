class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp=[1]*(len(nums))
        n=len(nums)
        
        
        
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    
                 #   print(dp[4])
                
        
        return max(dp)
        
        