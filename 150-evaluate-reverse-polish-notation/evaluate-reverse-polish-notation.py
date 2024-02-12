class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i=='+':
                x=st.pop()
                y=st.pop()
                st.append(x+y)
            elif i=='-':
                x=st.pop()
                y=st.pop()
                st.append(y-x)
            elif i=='*':
                x=st.pop()
                y=st.pop()
                st.append(x*y)
            elif i=='/':
                x=st.pop()
                y=st.pop()
                st.append(int(y/x))
            else:
                st.append(int(i))
        return st[-1]
