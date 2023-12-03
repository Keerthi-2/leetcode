class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(cur,temp):
            res.append(temp[:])

            for i in range(cur,len(nums)):
                temp.append(nums[i])
                print(temp)
                backtrack(i+1,temp)
                temp.pop()
        res=[]
        backtrack(0,[])

        return res
        