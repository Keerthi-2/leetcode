class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        c=max(nums)
        nums.remove(c)
        d=max(nums)
        nums.remove(d)
        a=min(nums)
        nums.remove(a)
        b=min(nums)

        return c*d-a*b
