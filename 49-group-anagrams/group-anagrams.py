class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getstring(s):
            f=[0]*26
            for i in s:
                f[ord(i)-97]+=1
            st=''
            for i in range(26):
                if f[i]!=0:
                    st+=str((chr(i+97))*f[i])
            return st
        d={}
        for i in strs:
            k=getstring(i)
            if k in d:
                d[k].append(i)
            else:
                d[k]=[i]
        
        return d.values()
        