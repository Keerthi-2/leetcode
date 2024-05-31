class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=0
        for i in nums:
            res=res^i
        
        pos_set_bit=0
        for i in range(31,-1,-1):
            if ((1<<i)&(res))!=0:
                pos_set_bit=i
                break
        res=[0,0]
        
        for i in nums:
            if (i&(1<<pos_set_bit))==0:
                res[0]^=i
            else:
                res[1]^=i
        res.sort()
        
        return res
                
            