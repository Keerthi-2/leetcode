class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        
        ans=""
        
        for i in s:
            ans+=str(ord(i)-96)
            
        
        cur=0
        print(ans)
        while(k>0):
            #print(ans)
            cur=0
            for i in range(len(ans)):
                cur+=int(ans[i])
            
            
            ans=str(cur)
            
            print(cur)
            #print(cur,ans)
            
            k-=1
            
        return cur