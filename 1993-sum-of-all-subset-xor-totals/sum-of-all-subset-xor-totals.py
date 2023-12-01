class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def bt(node,path):
            if node<=n:
                sub.append(path.copy())
            
            for i in range(node,n):
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
        res=0
        n=len(nums)
        sub=[]
        bt(0,[])
        print(sub)
        for i in sub:
            val=0
            for j in i:
                val=val^j
            
            res+=val
        
        return res





        