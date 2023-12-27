class Solution:
   def minCost(self,c, neededTime):
        n=len(c)
        ans=0
        for i in range(1,n):
            if c[i]==c[i-1]:
                ans+=min(neededTime[i],neededTime[i-1])
                neededTime[i]=max(neededTime[i],neededTime[i-1])
            
        return ans


        