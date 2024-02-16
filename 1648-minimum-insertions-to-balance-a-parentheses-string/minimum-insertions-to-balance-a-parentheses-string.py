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
                open+=1
            else:
                
                if(i+1<n and s[i+1]==')'):
                    if open>0:
                        open-=1
                    else:
                        ans+=1
                    i+=1
                else:
                    if open>0:
                        open-=1
                        ans+=1
                    else:
                        ans+=2
            i+=1
        if open>0:
            ans+=2*open
        return ans



