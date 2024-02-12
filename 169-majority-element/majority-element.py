class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=0
        c=1

        for i in range(len(nums)):
            if nums[m]==nums[i]:
                c+=1
            else:
                c-=1
            if c==0:
                c=1
                m=i
        
        return nums[m]

        