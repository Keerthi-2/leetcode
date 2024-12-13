class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        res=[(nums[i],i) for i in range(n)]
        
        res.sort()
        mark=[0]*n
        
        ans=0
        for i in range(n):
            number=res[i][0]
            index=res[i][1]
            
            if  not mark[index]:
                ans+=number
                mark[index]=True
                
                if index-1>=0:
                    mark[index-1]=True
                if index+1<n:
                    mark[index+1]=True
        
        return ans
                