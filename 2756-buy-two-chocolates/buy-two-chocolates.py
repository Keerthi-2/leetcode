class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        
        amount=money
        count=0
        s=0
        first_min=min(prices)
        prices.remove(first_min)
        second_min=min(prices)
        s+=first_min+second_min
        
        if s<=money:
            return money-s
        
        
        return money