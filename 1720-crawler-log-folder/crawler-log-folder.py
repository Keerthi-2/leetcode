class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        n=len(logs)
        i=0
        while(i<n):
            if logs[i]!="./":
                st.append(logs[i])
            while(len(st)>0 and i<n and st[-1]=="../"):
                st.pop()
                if len(st)>0:
                    st.pop()
                
            
            i+=1
        print(st)
        if len(st)>0 and st[-1]=='../':
            st.pop()
        
        return len(st)
        