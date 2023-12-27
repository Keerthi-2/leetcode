class Solution:
   def minCost(self,c, neededTime):
        n=len(c)
        previous_cost=0
        current_cost=0
        previous_color='A'
        previous_time=0
        ans=0
        for i in range(1,n+1):
            if previous_color==c[i-1]:
                current_cost=previous_cost+min(previous_time,neededTime[i-1])
                previous_time=max(previous_time,neededTime[i-1])

            else:
                current_cost=previous_cost
                previous_color=c[i-1]
                previous_time=neededTime[i-1]
            
            previous_cost=current_cost
        
        return current_cost


        