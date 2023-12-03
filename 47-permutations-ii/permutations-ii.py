class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def recur(nums, i):
            if i == len(nums):
                if nums not in ans:
                    ans.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                recur(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        recur(nums, 0)
        return ans
        