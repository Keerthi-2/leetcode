class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d={}

        res=0
        arr=[0]*100

        for i,j in dominoes:
            val=i*10+j if i>j else j*10+i
            res+=arr[val]
            arr[val]+=1
        
        return res
