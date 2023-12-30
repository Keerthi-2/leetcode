class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        d={}

        for i in words:
            for j in i:
                d[j]=d.get(j,0)+1
        
        l=len(words)

        for v in d.values():
            if v%l!=0:
                return False
        
        return True
        