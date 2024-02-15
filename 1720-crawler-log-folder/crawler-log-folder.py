class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        n=len(logs)
        i=0
        while(i<n):
            
            st.append(logs[i])
            while(len(st)>0 and i<n and (st[-1]=="../" or st[-1]=="./")):
                prev=st.pop()
                if len(st)>0 and prev=="../":
                    st.pop()
    
            i+=1
        
        
        return len(st)
        