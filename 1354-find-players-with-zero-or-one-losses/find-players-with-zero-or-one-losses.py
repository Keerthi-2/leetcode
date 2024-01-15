class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        min_node=10**9
        max_node=0
        for w,l in matches:
            if l in d:
                d[l].append(w)
            else:
                d[l]=[w]
            if w not in d:
                d[w]=[]
        print(d)
        ans=[[],[]]
        won=[]
        one=[]
        
        for i in d:
            if len(d[i])==0:
                ans[0].append(i)
            if len(d[i])==1:
                ans[1].append(i)
            
        ans[0].sort()
        ans[1].sort() 
        return ans

        