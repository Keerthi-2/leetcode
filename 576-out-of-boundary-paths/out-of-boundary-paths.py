class Solution:
    def findPaths(self, m: int, n: int, M: int, i: int, j: int) -> int:
        
        memo={}

        def recur(m,n,M,i,j):
            if i==m or j==n or i<0 or j<0:
                return 1
            if M==0:
                return 0
            if (i,j,M) in memo:
                return memo[(i,j,M)]
            memo[(i,j,M)]=(recur(m,n,M-1,i+1,j)+recur(m,n,M-1,i,j+1)+recur(m,n,M-1,i-1,j)+recur(m,n,M-1,i,j-1))%(10**9+7)

            return memo[(i,j,M)]

        return recur(m,n,M,i,j)%(10**9+7)
        