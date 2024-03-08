class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        c=[0]*101

        for i in nums:
            c[i]+=1
        
        m=max(c)

        ans=0

        for i in c:
            if i==m:
                ans+=i
        
        return ans