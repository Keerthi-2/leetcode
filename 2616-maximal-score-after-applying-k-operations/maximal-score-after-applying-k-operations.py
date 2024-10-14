from heapq import heapify,heappush,heappop
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        res=0
        for i in range(len(nums)):
            nums[i]=nums[i]*-1
        heapify(nums)
        while(k>0):
         #   print(nums)
            if len(nums)>0:
                val=heappop(nums)
                val=val*-1
                res+=val

                heappush(nums,-1*(val//3+(val%3!=0)))
                k-=1
            
        return res
        
        
        