class Solution:
   def minCost(self,c, neededTime):
        n=len(c)
        dp=[0]*(n+1)
        previous_color='A'
        previous_time=0
        ans=0
        for i in range(1,n+1):
            if previous_color==c[i-1]:
                dp[i]=dp[i-1]+min(previous_time,neededTime[i-1])
                previous_time=max(previous_time,neededTime[i-1])

            else:
                dp[i]=dp[i-1]
                previous_color=c[i-1]
                previous_time=neededTime[i-1]
        
        return dp[n]


        