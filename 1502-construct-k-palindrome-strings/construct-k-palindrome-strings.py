class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        
        if len(s)<k:
            return False
        
        odd_count=0
        for i,val in d.items():
            if val%2:
                odd_count+=1
        
        if odd_count>k:
            return False
        
        return True
