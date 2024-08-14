class Solution:
    ans=False
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis=[0]*n
        def dfs(d,cur,dest):
            #print(cur,d)
            if cur==dest:
                self.ans=True
            vis[cur]=1
            for i in d[cur]:
                if vis[i]==0:
                    dfs(d,i,dest)
            
           
            
                
        if source==destination:
            return True
            
        d={}
       
        for u,v in edges:
            
            if u in d:
                d[u].append(v)
            else:
                d[u]=[v]
            
            if v in d:
                d[v].append(u)
            else:
                d[v]=[u]
                
        dfs(d,source,destination)
        return self.ans
        