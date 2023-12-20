class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        
        
        s=0
        
        freq=[0]*100

        for i in prices:
            freq[i-1]+=1
        print(freq)
        first_min,second_min=0,0
        for i in range(1,101):
            if first_min==0 and freq[i-1]>0:
                first_min=i
                freq[i-1]-=1
            if second_min==0 and freq[i-1]>0:
                second_min=i
                break
        s+=first_min+second_min
        print(first_min,second_min)
        if s<=money:
            return money-s

        
        
        return money