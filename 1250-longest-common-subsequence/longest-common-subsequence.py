class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        n1=len(s1)
        n2=len(s2)

        dp=[0 for i in range(n2+1)]

        for i in range(1,n1+1):
            new_dp=[0 for i in range(n2+1)]
            for j in range(1,n2+1):
                if s1[i-1]==s2[j-1]:
                    new_dp[j]=1+dp[j-1]
                else:
                    new_dp[j]=max(dp[j],new_dp[j-1])
            dp=new_dp
        
        return dp[-1]

