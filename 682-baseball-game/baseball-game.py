class Solution:
    def calPoints(self, op: List[str]) -> int:
        st=[]
        for i in op:
            if i=='D':
                top=st[-1]*2
                st.append(top)
            elif i=='C':
                st.pop()
            elif i=='+':
                
                top=st[-1]+st[-2]
                st.append(top)
            else:
                st.append(int(i))
        return sum(st)

        