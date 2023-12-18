class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        return (x:=sorted(nums))[-1]*x[-2]-x[0]*x[1]