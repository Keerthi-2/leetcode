import collections
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n=len(formula)
        st=[(collections.Counter())]
        i=0

        while(i<n):
            c=formula[i]
            if c=='(':
                st.append(collections.Counter())
                i+=1
            elif c==')':
                cur=st.pop()

                i+=1
                start=i
                while(i<n and formula[i].isdigit()):
                    i+=1
                
                number=int(formula[start:i]) if formula[start:i] else 1

                for atom in cur:
                    st[-1][atom]+=cur[atom]*number
            
            else:

                atom=c
                i+=1
                start=i

                while(i<n and formula[i].islower()):
                    i+=1
                
                atom+=formula[start:i]

                start=i
                while(i<n and formula[i].isdigit()):
                    i+=1
                number=int(formula[start:i]) if formula[start:i] else 1

                st[-1][atom]+=number
        
        ans=""
        dic=st[-1]

        for atom in sorted(dic):
            ans+=atom
            if dic[atom]>1:
                ans+=str(dic[atom])
        
        return ans



                