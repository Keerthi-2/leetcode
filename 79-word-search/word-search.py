class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(board,word,i,j,k):
            if k==len(word): 
                print(i,j,k)
                return True
            if len(word)==0 and word[0]==board[i][j]: return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[i]) or (board[i][j]!=word[k]): return False

            temp=False
            board[i][j]='--'
            dx=[0,0,1,-1]
            dy=[1,-1,0,0]
            for ind in range(0,4):
                x=i+dx[ind]
                y=j+dy[ind]
                
                temp=temp or dfs(board,word,x,y,k+1)
            board[i][j]=word[k]
            return temp


        m=len(board)
        if m==0: return False
        if len(word)==0: return False
        n=len(board[0])

        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j]:
                    if dfs(board,word,i,j,0)==True:
                        print(i,j)
                        return True
            
        return False