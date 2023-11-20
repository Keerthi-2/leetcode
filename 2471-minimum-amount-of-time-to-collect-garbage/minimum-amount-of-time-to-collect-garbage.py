class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        count_m,count_p,count_g=0,0,0

        m,p,g=-1,-1,-1
        d={}
        
        res=0

        for i in range(len(garbage)-1,-1,-1):
            cur=garbage[i]
            if 'M' in cur:
                count_m=cur.count('M')
                res+=count_m
                m=max(m,i)
            if 'G' in cur:
                count_g=cur.count('G')
                res+=count_g
                g=max(g,i)
            if 'P' in cur:
                count_p=cur.count('P')
                res+=count_p
                p=max(p,i)
        
        for i in range(1,len(travel)):
            travel[i]=travel[i]+travel[i-1]

        if m>0:
            
            res+=travel[m-1]
        if p>0:   
            res+=travel[(p-1)]
        if g>0:   
            res+=travel[(g-1)]

        return res
            


            
        