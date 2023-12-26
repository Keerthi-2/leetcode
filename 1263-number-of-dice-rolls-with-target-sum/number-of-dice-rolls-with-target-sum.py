class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mod=10**9+7
        def recursion(n,k,t):
            if n==0 and t==0:
                return 1
            if n==0 or t<=0:
                return 0
            
            if dp[n][t]!=-1:
                return dp[n][t]%mod
            ways=0
            for i in range(1, k + 1):
                ways = (ways + recursion(n - 1, k, t - i)) % mod

            dp[n][t]=ways%mod
            return ways 
        dp=[[-1 for j in range(target+1)]for i in range(n+1)]
        return recursion(n,k,target)        