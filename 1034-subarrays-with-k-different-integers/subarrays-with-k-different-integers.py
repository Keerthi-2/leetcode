class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums,k):
            ans=0
            r=0
            l=0
            d={}
            for r in range(len(nums)):
                if nums[r] in d:
                    d[nums[r]]+=1
                else:
                    d[nums[r]]=1
                while(l<=r and len(d)>k):
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        d.pop(nums[l])
                    l+=1
                ans+=r-l
                
            return ans
        
        return atmost(nums,k)-atmost(nums,k-1)
