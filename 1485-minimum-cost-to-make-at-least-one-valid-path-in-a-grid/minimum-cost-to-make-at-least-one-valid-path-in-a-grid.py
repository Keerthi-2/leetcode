from heapq import heapify,heappush,heappop
class Solution:
    dirs=[(0,1),(0,-1),(1,0),(-1,0)]
    def minCost(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        pq=[(0,0,0)]
        heapify(pq)
        vis=[[False for j in range(m)]for i in range(n)]

        cost=0
        while pq:
            cur,x,y=heappop(pq)

            if vis[x][y]:
                print(x,y,"contin")
                continue
            if x==n-1 and y==m-1:
                return cur
            vis[x][y]=True
            for didx,(x1,y1)in enumerate(self.dirs):
                dx=x+x1
                dy=y+y1

                if 0<=dx<n and 0<=dy<m and vis[dx][dy]==False:
                    new_cost=cur+((didx+1)!=grid[x][y])
                    heappush(pq,(new_cost,dx,dy))
                    
        
        return 0



        