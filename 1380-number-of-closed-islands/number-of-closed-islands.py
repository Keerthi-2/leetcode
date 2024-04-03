class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited=[]
        dirx=[-1,0,1,0]
        diry=[0,1,0,-1]

        m=len(grid)
        n=len(grid[0])

        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n:
                return False
            
            if (x,y) in visited:
                return True
            
            if grid[x][y]==1 or (x,y) in visited:
                return True

            visited.append((x,y))

            ans=True
            for idx in range(len(dirx)):
                if dfs(x+dirx[idx],y+diry[idx])==False:
                    ans= False
            if(i==5 and j==4):
                print(ans)
            return ans

        res=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    if (i,j) in visited:
                        continue
                    if dfs(i,j):
                        res=res+1
        print(visited)
        return res