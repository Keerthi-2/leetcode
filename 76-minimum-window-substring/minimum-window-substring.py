class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        distinct=len(d)
        start=0
        end=len(s)
        i=0
        ans=10**7
        for j in range(len(s)):
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    distinct-=1

            while distinct==0:

                if j-i+1<end-start+1:
                    ans=j-i+1
                    start=i
                    end=j
                if s[i] in d:
                    d[s[i]]+=1

                    if d[s[i]]==1:
                        distinct+=1
                i+=1
        if ans==10**7:
            return ""
        return s[start:end+1]
