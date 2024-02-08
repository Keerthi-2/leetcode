class Solution:
    def numSquares(self, n: int) -> int:
        
        def solve(n,dp):
            if n==0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            ans=10**7
            for i in range(1,int(n**0.5)+1):
                ans=min(ans,1+solve(n-i*i,dp))
                dp[n]=ans
            return dp[n]


        dp=[-1]*(n+1)
        return solve(n,dp)
        
        