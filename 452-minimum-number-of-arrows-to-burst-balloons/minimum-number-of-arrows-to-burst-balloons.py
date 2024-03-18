class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x:x[1])

        res=0
        cur=-float('inf')

        for i in points:
            if i[0]>cur:
                cur=i[1]
                res+=1
        return res
        
        
        