class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        s=nums[0]
        n=len(nums)
        res=[-1]*(n-k+1)
        flag=True
        
        res_ind=0
        for i in range(1,k):
            s+=nums[i]
            
            if nums[k-1]-nums[0]!=(k-1):
                flag=False
                
                   
        
        if flag:
            print(0)
            val=k/2*(nums[0]+nums[k-1])
            
            if int(val)==s:
                res[res_ind]=nums[k-1]
        
        res_ind+=1
        
        end=k
        start=0
        
        while(end<n):
            
            s-=nums[start]
            s+=nums[end]
            
            
            start+=1
            
            if (nums[end]-nums[start])!=(k-1):
                res[res_ind]=-1
            else:
                val=k/2*(nums[start]+nums[end])
                
                if int(val)==s:
                    res[res_ind]=nums[end]

            res_ind+=1
            end+=1
        
        return res
            
                
                