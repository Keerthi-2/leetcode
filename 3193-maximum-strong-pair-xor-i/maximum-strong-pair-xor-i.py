class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(len(nums)):
            xor=0
            cur=nums[i]
            for j in range(i+1,n): 
                if abs(cur-nums[j])<=min(cur,nums[j]):
                    res=max(res,(cur^nums[j]))
        return res
                
                
                
        