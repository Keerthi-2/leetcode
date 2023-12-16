class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d1={}
        for j in t:
            if j in d1:
                d1[j]+=1
            else:
                d1[j]=1
        for i in range(len(s)):
            if s[i] in d and s[i] in t:
                if d[s[i]]!=d1[s[i]]:
                    return False
            else:
                return False
        
        return True
        
        