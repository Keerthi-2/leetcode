class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i=0
        d={}
        ans=0
        for j in range(len(nums)):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                d[nums[j]]=1
            while(i<j and d[nums[j]]>k):
                d[nums[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans