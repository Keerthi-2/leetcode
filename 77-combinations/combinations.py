class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        def comb(ind,temp):
            if len(temp)==k:
                res.append(temp[:])
                return
            
            for i in range(ind,n+1):
                temp.append(i)
                comb(i+1,temp)
                temp.pop()
        
        comb(1,[])
        return res
        