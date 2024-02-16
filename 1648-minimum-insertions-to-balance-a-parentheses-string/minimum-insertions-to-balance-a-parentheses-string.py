class Solution:
    def minInsertions(self, s: str) -> int:
        st=[]
        i=0
        ans=0
        open=0
        close=0
        n=len(s)
        while(i<n):
            if s[i]=='(':
                st.append(s[i])
            else:
                
                if(i+1<n and s[i+1]==')'):
                    if len(st):
                       st.pop()
                    else:
                        ans+=1
                    i+=1
                else:
                    if len(st)>0:
                        st.pop()
                        ans+=1
                    else:
                        ans+=2
            i+=1
        if len(st)>0:
            ans+=2*len(st)
        return ans



