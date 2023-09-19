class Solution:
    
    # very good approach i like it a lot
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind=abs(nums[i])
            if nums[ind]<0:
                return ind
            else:
                nums[ind]=nums[ind]*-1
            
        return 0