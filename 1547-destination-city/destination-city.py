class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        d={}
        nodes=set()
        for i in range(len(paths)):
            s=paths[i][0]
            j=paths[i][1]
            print(s,j)
            nodes.add(s)
            nodes.add(j)
            if j in d:
                d[j]+=1
            else:
                d[j]=1
            if s in d:
                d[s]-=1
            else:
                d[s]=-1
        print(d)
        for k in d:
            if d[k]>0:
                return k
        