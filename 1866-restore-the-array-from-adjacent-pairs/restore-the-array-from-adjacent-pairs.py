class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d={}
        for i,j in adjacentPairs:
            if i in d:
                d[i].append(j)
            else:
                d[i]=[j]
            if j in d:
                d[j].append(i)
            else:
                d[j]=[i]
        print(d)
        root=None
        for key in d:
            if len(d[key])==1:
                root=key
        
        def dfs(root,prev):
            ans.append(root)
            vis.add(root)
            for neigh in d[root]:
                if neigh not in vis:
                    dfs(neigh,root)



        vis=set()
        ans=[]
        dfs(root,None)
        return ans
        

        