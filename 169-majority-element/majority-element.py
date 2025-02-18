class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = -1
        votes = 0

        n = len(nums)

        for i in range(n):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if candidate != nums[i]:
                    votes -= 1
                else:
                    votes += 1
        
        count = 0

        for i in range(n):
            if candidate == nums[i]:
                count += 1
        
        if count>(n//2):
            return candidate
        
        return -1

        