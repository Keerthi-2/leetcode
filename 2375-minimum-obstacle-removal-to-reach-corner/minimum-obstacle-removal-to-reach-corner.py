class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # minimum removed obstacles table
        dp = [[inf for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        # removed obstacles count, i, j
        heap = [(0, 0, 0)]
		
        while heap:
            removed, i, j = heappop(heap)
            if i == m-1 and j == n-1:
                return removed
            for ii, jj in [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]:
                if (0 <= ii < m and 0 <= jj < n) and grid[ii][jj] + removed < dp[ii][jj]:
                    dp[ii][jj] = grid[ii][jj] + removed
                    heappush(heap, (dp[ii][jj], ii, jj))
            #print(dp)
        return dp[-1][-1]
  