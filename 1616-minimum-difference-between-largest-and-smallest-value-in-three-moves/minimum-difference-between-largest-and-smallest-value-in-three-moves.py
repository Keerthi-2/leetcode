class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        res=float('inf')
        if len(nums)<=3:
            return 0
        n=len(nums)
        for i in range(4):
            res=min(res,nums[n-4+i]-nums[i])
        return res
        