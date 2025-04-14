class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,0)
        dp=[0 for i in range(n+1)]
        dp[0]=0
        dp[1]=nums[1]
        for i in range(2,n+1):
            dp[i]+=max((nums[i]+dp[i-2]),dp[i-1])
        return dp[n]
