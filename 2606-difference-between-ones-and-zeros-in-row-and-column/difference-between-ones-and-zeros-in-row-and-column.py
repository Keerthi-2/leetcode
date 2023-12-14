class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        ones_row=[0]*n
        ones_col=[0]*m

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ones_row[i]+=1
                    ones_col[j]+=1
        

        for i in range(n):
            for j in range(m):
                grid[i][j]=ones_row[i]+ones_col[j]-(n-ones_row[i])-(m-ones_col[j])
        
        return grid
        