class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        n=len(board)
        m=len(board[0])
        dy=[-1,0,1,1,1,0,-1,-1]
        dx=[-1,-1,-1,0,1,1,1,0]
        def count(x,y,n,m):
            ans=0
            for i in range(8):
                
                nx=dx[i]+x
                ny=dy[i]+y

                if nx>=0 and nx<n and ny>=0 and ny<m and (board[nx][ny]==-1 or board[nx][ny]==1):
                    ans+=1
            
            return ans

        for i in range(n):
            for j in range(m):
                cur=count(i,j,n,m)
                
                print(i,j,cur)
                val=board[i][j]
                
                if val==1: 
                    if (cur<2 or cur>3):
                        board[i][j]=-1
                    
                else:
                    if cur==3:
                        board[i][j]=2
                    
                        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
        