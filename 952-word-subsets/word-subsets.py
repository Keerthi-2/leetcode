class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        
        def count(w):
            ans=[0]*26
            for i in w:
                ans[ord(i)-97]+=1
            
            return ans
        
        bmax=[0]*26
        for b in B:
            for i,c in enumerate(count(b)):
                bmax[i]=max(bmax[i],c)
        
        print(bmax)
        ans=[]
        for a in A:
            flag=True
            arr=count(a)
            print(arr)
            for i in range(26):
                if arr[i]<bmax[i]:
                    flag=False
                    break
            if flag:
                ans.append(a)
        
        return ans

