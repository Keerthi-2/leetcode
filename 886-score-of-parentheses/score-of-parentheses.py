class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0
        res=0
        n=len(s)
        st=[]        
        for i in range(n):
            if s[i]=='(':
                st.append("(")
            else:
               
                if len(st)>0 and st[-1]=='(':
                    st.pop()
                    st.append(1)
                else:
                    while(len(st)>0 and st[-1]!='('):
                        ans+=st.pop()
                    st.pop()
                    st.append(2*ans)
                    ans=0
        res=0
        print(st,ans)
        while(st):
            res+=st.pop()
       
        return res


        