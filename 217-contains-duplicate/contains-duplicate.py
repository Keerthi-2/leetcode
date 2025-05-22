class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d={}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for k,v in d.items():
            if v >= 2:
                return True
        
        return False