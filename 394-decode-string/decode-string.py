class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        n=0
        for i in s:
            
            if i!=']':
                st.append(i)
                
            else:
                
            
                nums=[]
                chars=[]
                all=[]

                while(len(st)>0 and st[-1]!='['):
                    if(st[-1].isdigit()==False):
                        chars.append(st.pop())
                    
                st.pop()
                #  3 2 1       # in stack 3 2 1  1+2*10+     11+  31
                while(len(st)>0 and st[-1].isdigit()):
                    nums.append(st.pop())

                chars=chars[::-1]
                nums=nums[::-1]
                ch=''.join(chars)
                n=int(''.join(nums))
                
                
                
                st.append(ch*n)
        
        return ''.join(st)

        