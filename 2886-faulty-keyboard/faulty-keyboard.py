class Solution:
    def finalString(self, s: str) -> str:
        
        n=len(s)
        res=[""]*n
        l,r=0,n-1
        flag=1
        for i in range(n-1,-1,-1):
            cur=s[i]
            
            if cur=='i':
                flag=flag^1
            elif flag==1:
                res[r]=cur
                r-=1
            else:
                res[l]=cur
                l+=1
        print(res)
        return "".join(res)
                
            
        