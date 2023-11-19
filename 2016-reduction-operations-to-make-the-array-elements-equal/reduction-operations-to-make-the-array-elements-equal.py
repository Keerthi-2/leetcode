class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
       
        res=0
        nums.sort()
        up=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                up+=1
            res+=up

        return res

        