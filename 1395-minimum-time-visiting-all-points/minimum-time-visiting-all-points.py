class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res=0

        for i in range(1,len(points)):
            x_dist=abs(points[i][0]-points[i-1][0])
            y_dist=abs(points[i][1]-points[i-1][1])

            res+=max(x_dist,y_dist)
        
        return res
        