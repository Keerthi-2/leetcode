class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        ans=0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                cur=mat[i][j]
                if cur==1:
                    #print(i,j)
                    f=0
                    for c in range(len(mat[i])):
                        if mat[i][c]!=0:
                            f+=1
                            
                    
                    for r in range(0,len(mat)):
                        if mat[r][j]!=0:
                            f+=1
                            
                    print(i,j,cur)
                    if f==2:
                        print(cur)
                        ans+=1
        
        return ans
        