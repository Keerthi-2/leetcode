class Solution:
    def check(self, nums: List[int]) -> bool:
        one_peak=0
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                one_peak+=1

        if nums[0] < nums[n - 1]:
            one_peak += 1
        if one_peak<=1:
            return True

        return False               
