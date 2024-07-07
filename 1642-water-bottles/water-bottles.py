class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n=numBottles
        ans=n
        while(n>=numExchange):
            div=n//(numExchange)
            rem=n%(numExchange)
            ans+=div
            n=div+rem
        
        return ans

        