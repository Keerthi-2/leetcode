class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        

        #  1  2  3  4  5         1 2 3  2 3 4   3 4 5  1 2 3 4  2 3 4 5  5

        #  1 2 3 4 5 6       123 234 345 456  1234 2345 3456  12345 23456 123456

        res=0
        prev=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                prev+=1
                res+=prev
            else:
                prev=0
        return res