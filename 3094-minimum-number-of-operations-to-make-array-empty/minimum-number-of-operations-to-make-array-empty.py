class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d={}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        ans=0
        print(d)
        for k in list(d.keys()):
            v=d[k]
            if v==1:
                return -1
            ans+=(ceil(v/3))
        
        
        return ans
        
