class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        i=0
        j=0
        l=len(word1)
        l1=len(word2)
        cur=0
        cur1=0
        while(i<l and j<l1):
            if word1[i][cur]!=word2[j][cur1]:
                return False
            cur+=1
            cur1+=1
            
            if cur==len(word1[i]):
                cur=0
                i+=1
            if cur1==len(word2[j]):
                cur1=0
                j+=1
        
        return i==len(word1) and j==len(word2)