class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        d1=Counter(word1)
        d2=Counter(word2)
        v1=sorted(d1.values())

        v2=sorted(d2.values())
        k1=d1.keys()
        k2=d2.keys()
        print(k1,k2,type(k1),set(k1)==set(k2))
        print(v1,v2)
        return (k1)==(k2) and v1==v2



        