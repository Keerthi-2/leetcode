class Solution:
    def sortVowels(self, s: str) -> str:
        
        v=""
        vow=['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in vow:
                v=v+i
        #print(v)
        l=sorted(list(v))
        #print(l)
        res=""
        ind=0
        for i in s:
            if i in vow:
                res+=l[ind]
                ind+=1
            else:
                res+=i
        return res
                
        
        