class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        m=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c=c+1
            else:
                c=c-1
            if c in d.keys():
                m=max(m,i-d[c])
            else:
                d[c]=i
        print(d)
        return m
        
        
        
        
        