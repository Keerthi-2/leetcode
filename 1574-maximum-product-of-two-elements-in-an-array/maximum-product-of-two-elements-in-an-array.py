class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=0

        for i in range(0,len(nums)):
            count=nums[i]-1
            for j in range(i+1,len(nums)):
                ans=max(ans,count*(nums[j]-1))
            
        return ans

        