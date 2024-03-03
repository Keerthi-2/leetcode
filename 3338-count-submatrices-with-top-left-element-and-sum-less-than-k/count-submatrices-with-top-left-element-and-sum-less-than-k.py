class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        ans=0
        new_mat=grid
        
        new_mat[0][0]=grid[0][0]
        if grid[0][0]<=k:
            ans+=1
        for j in range(1,len(grid[0])):
            new_mat[0][j]+=new_mat[0][j-1]
            print(grid[0][j])
            if new_mat[0][j]<=k:
                ans+=1       
        print(ans)       
        for i in range(1,len(grid)):
            new_mat[i][0]+=new_mat[i-1][0]
            
            if new_mat[i][0]<=k:
                ans+=1
            
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                
                new_mat[i][j]+=new_mat[i-1][j]+new_mat[i][j-1]-new_mat[i-1][j-1]
                
                
                if new_mat[i][j]<=k:
                    ans+=1
        print(grid)
        return ans
        
        
                