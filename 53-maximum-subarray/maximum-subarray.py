class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum = 0
        max_sum = float('-inf')
        threshold = 0

        for i in range(len(nums)) :
            cur_sum += nums[i]
            max_sum = max(max_sum,cur_sum)

            if(cur_sum<threshold):
                cur_sum=0

        return max_sum
        