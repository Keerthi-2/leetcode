class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        c=0
        s=sum(nums)
        s1=0
        for i in range(len(nums)-1):
            
            s1+=nums[i]
            s=s-nums[i]
            if s1>=s:
                c+=1
        return c