class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        def f1(w,x):
            
            for i in range(len(w)):
                cur=w[i]
                if x in cur:
                    ans.append(i)
        ans=[]
        f1(words,x)
        return ans
        