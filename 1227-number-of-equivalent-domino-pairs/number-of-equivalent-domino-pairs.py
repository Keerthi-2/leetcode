class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        

        res=0
        arr={}
       
        for i,j in dominoes:
            val=str(i)+"#"+str(j) if i>j else str(j)+'#'+str(i)
            if val in arr:
                res+=arr[val]
            arr[val]=arr.get(val,0)+1
        
        return res
