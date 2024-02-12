class Solution:
    def simplifyPath(self, path: str) -> str:
        arr=path.split("/")
        st=[]
        
        for i in arr:
            if i=='..':
                if len(st)>0:
                    st.pop()
            elif i=='.' or i=='':
                continue
            else:
                st.append(i)
        res=''

        if len(st)==0:
            return "/"
        for i in st:
            res+="/"+i
        return res
            
            
        