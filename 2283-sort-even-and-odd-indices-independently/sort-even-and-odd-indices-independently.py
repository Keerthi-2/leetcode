class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        e=0
        o=0
        for i in range(len(nums)):
            if i%2:
                odd.append(nums[i])
            else:
                even.append(nums[i])
                
        odd.sort()
        even.sort()
        o=len(odd)-1
        
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[e]
                e+=1
            else:
                nums[i]=odd[o]
                o-=1
        return nums
                
        
            
        