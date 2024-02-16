class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        res=[0]*len(seq)
        count=0
        for i in range(len(seq)):
            if seq[i]=='(':
                count+=1
                res[i]=count%2
            else:
                res[i]=count%2
                count-=1
        
        return res
        