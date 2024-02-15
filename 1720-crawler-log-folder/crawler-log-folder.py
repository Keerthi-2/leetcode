class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        n=len(logs)
        i=0
        while(i<n):
            while(len(st)>0 and i<n and logs[i]=="../"):
                st.pop()
                i+=1
            if i<n and logs[i]!="./":
                if logs[i]!="../": 
                    st.append(logs[i])
            i+=1
        print(st)
        
        return len(st)
        