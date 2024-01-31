class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        n=len(temperatures)
        res=[0]*len(temperatures)
        
        for i in range(n):
            while(len(s) and temperatures[s[-1]]<temperatures[i]):
                ind=s.pop(-1)
                res[ind]=i-ind
            s.append(i)
        return res
                
        