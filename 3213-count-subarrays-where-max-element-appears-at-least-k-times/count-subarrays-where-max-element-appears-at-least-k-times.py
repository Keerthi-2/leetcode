class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m=max(nums)
        n=len(nums)
        i=0
        ans=(n*(n+1))//2
        cur=0
        max_ele_count=0
        for j in range(n):
            if nums[j]==m:
                max_ele_count+=1
            while(max_ele_count>=k):
                if nums[i]==m:
                    max_ele_count-=1
                i+=1
            cur+=j-i+1
        
        return ans-cur
            
