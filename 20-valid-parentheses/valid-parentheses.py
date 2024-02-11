class Solution:
    def isValid(self, s: str) -> bool:

        
        st=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if len(st)>0:
                    cur=st[-1]
                    if i==')' and cur=='(':
                        st.pop()
                    elif i=='}' and cur=='{':
                        st.pop()
                    elif i==']' and cur=='[':
                        st.pop()
                    else:
                        return False
                else:
                    return False
        return len(st)==0


