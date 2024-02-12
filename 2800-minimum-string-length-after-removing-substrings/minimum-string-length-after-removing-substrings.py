class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        n=len(s)
        for i in range(n):
            if len(st)>0 and st[-1]=='A' and s[i]=='B':
                st.pop()
            elif len(st)>0 and st[-1]=='C' and s[i]=='D':
                st.pop()
            else:
                st.append(s[i])

        print(st,len(st))
        return len(st)

        