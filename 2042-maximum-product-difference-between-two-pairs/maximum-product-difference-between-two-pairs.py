class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        nums.sort()

        c,d=nums[-1],nums[-2]
        a,b=nums[0],nums[1]

        return c*d-a*b