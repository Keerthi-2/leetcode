class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        out=[0]*(n+1)
        ind=[0]*(n+1)
        for i in trust:

            out[i[0]]+=1
            ind[i[1]]+=1
        
        
        for i in range(1,n+1):
            if out[i]==0 and ind[i]==n-1:
                print(i)
                return i
        
        return -1
        