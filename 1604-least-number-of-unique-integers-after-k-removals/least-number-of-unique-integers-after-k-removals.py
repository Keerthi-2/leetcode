class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        temp=dict(sorted(d.items(),key=lambda x:x[1]))
        for key,val in temp.items():
            if val<=k:
                k-=val
                d.pop(key)
            if k==0:
                return len(d)

        return len(d)
