class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(n):
            ans=max(ans,nums[n-i-1]+nums[i])
        return ans
        