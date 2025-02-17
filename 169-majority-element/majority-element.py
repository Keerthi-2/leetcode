class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n=len(nums)

        candidate=-1
        vote=0

        for i in range(n):
            if vote == 0:
                candidate = nums[i]
                vote = 1
            else:
                if candidate == nums[i]:
                    vote += 1
                else:
                    vote -= 1
        
        count = 0

        for i in range(n):
            if candidate == nums[i]:
                count += 1
        
        if count>(n//2):
            return candidate
        
        return -1