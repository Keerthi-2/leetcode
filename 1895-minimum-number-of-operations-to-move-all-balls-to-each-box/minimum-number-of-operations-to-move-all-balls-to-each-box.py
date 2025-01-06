class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        res=[0]*n

        for i in range(n):
            cur=0
            for j in range(0,n):
                if i!=j:
                    if boxes[j]=='1':
                        cur+=abs(j-i)


            res[i]=cur

        return res