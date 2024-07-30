class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        ans=0
        
        st=[]
        
        for i in range(n):
            
            if(len(st)>0 and st[-1]=='b' and s[i]=='a'):
                ans+=1
                st.pop()
            else:    
            
                st.append(s[i])
        
        return ans