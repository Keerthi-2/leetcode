class Solution:
    def findTheDifference(dlf, s: str, t: str) -> str:
        if len(s)==0:
            return t
        s1=list(s)
        s2=list(t)
        s1.sort()
        s2.sort()
        print(s1,s2)
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return s2[i]
        return s2[len(s1)]


        