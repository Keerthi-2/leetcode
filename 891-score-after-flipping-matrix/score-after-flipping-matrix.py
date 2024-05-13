class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        ans=0
        
        r=len(grid)
        c=len(grid[0])
        
        for j in range(r):
            if grid[j][0]==0:
                for i in range(c):
                    grid[j][i]=grid[j][i]^1
        
        
        for j in range(1,c):
            count_zero=0
            
            for i in range(r):
                if grid[i][j]==0:
                    count_zero+=1
                
            if count_zero>r-count_zero:
                for i in range(r):
                    grid[i][j]^=1
        
        
        for i in range(r):
            for j in range(c):
                cols=grid[i][j]<<(c-j-1)
                ans+=cols
        
        return ans
            
        