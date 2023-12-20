class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        amount=money
        count=0
        s=0
        s+=prices[0]+prices[1]
        
        if s<=money:
            return money-s
        
        
        return money