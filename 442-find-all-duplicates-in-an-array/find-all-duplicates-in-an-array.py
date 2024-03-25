class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]

        for i in nums:
            cur=abs(i)
            if nums[cur-1]<0:
                res.append(cur)
            else:
                nums[cur-1]*=-1
        return res
