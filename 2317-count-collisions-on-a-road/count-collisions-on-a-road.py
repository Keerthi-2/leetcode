class Solution:
    def countCollisions(self, d: str) -> int:
        ans=0
        n=len(d)
        st=[]
        for i in range(len(d)):
            if len(st)>0 and st[-1]=='R' and d[i]=='L':
                ans+=2
                st[-1]='S'
                
            elif len(st)>0 and st[-1]=='R' and d[i]=='S':
                ans+=1
                st[-1]='S'
                
            elif len(st)>0 and st[-1]=='S' and d[i]=='L':
                ans+=1
                
                
            else:
                st.append(d[i])
            while(len(st)>1 and st[-1]=='S' and st[-2]=='R'):
                ans+=1
                st.pop()
                st[-1]='S'

        print(st)
        
        return ans