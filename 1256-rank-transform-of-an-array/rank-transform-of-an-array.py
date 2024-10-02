class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        
        n=len(arr)
        res={}
        cur=sorted(arr)
        rank=1
        for i in range(n):
            
            if i>0 and cur[i]>cur[i-1]:
                rank+=1
                
            res[cur[i]]=rank
        
        for i in range(n):
            arr[i]=res[arr[i]]
        print(arr,cur)
        return arr
            
            