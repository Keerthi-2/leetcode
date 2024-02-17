class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        comb=[]
        for i in range(len(positions)):
            comb.append([positions[i],healths[i],directions[i]])
        comb.sort()
        ans=[]
        st=[]
        n=len(positions)
        i=0
       
        count_r=0
        count_l=0
        d={}
        while(i<n):
            if comb[i][-1]=='R':
                st.append(comb[i])
                
            else:
                
                
                while(len(st)>0 and st[-1][2]=='R' and st[-1][1]<comb[i][1]):
                    st.pop()
                    comb[i][1]-=1
                
                if len(st)>0:
                    
                    if st[-1][1]==comb[i][1]:
                        st.pop()
                    else:
                        st[-1][1]-=1
                else:
                    d[comb[i][0]]=comb[i][1]
            i+=1
       
        
        cur=[]
        
        print(st)
        while(len(st)>0):
            p=st.pop()
            d[p[0]]=p[1]
        
        for i in range(n):
            if positions[i] in d:
                ans.append(d[positions[i]])

        return ans




        