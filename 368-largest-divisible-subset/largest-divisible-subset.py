class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        dp=[[] for i in range(len(nums)+1)]
        n=len(nums)
        for i in range(0,n):
            subset=[]
            for j in range(0,i):
                if nums[i]%nums[j]==0 and len(dp[j])>=len(subset):
                    subset=dp[j]
            dp[i]=subset+[nums[i]]
            if len(dp[i])>len(ans):
                ans=dp[i]
                    
        print(dp)   
        
        return ans


        