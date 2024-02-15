class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans=-1
        nums.sort()
        n=len(nums)
        prev=0
        for i in range(n):
            if i>=2 and prev>nums[i]:
                ans=prev+nums[i]
            prev+=nums[i]
        
        return ans

        