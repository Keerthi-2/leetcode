class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x2=-1
        y2=-1

        x1=10000
        y1=10000

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==1:
                    x1=min(x1,i)
                    y1=min(y1,j)
                    x2=max(x2,i)
                    y2=max(y2,j)
        
        print(x1,y1,x2,y2)
        return (x2-x1+1)*(y2-y1+1)