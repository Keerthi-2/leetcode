class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=0

        left=0
        target=0
        cur=0
        for right in range(len(nums)):
            cur+=nums[right]
            target=nums[right]

            while((right-left+1)*target-cur>k):
                cur-=nums[left]
                left+=1
            res=max(res,right-left+1)
        
        return res
        
        