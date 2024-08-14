class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        # 1 4 10 25 25   1 4  3  
        
        nums.sort()
        n=len(nums)
        l=1   # 1 1  5 1+5-1
        
        ans=0
        for i in range(0,n):
            if nums[i]>l:
                r=min(nums[i]-1,l+k-1)

                cnt=(r-l)+1
                
                ans+=((l+r)*(cnt/2))

                k-=cnt

                if k==0:
                    return int(ans)
            l=nums[i]+1
        
        print(k,ans)
        
        if k>0:
            ans+=(l+l+k-1)*(k/2)
        
        return int(ans)
            
        
            