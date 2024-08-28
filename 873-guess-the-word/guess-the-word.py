# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        l=0
        i=0
        while(i<10 and l!=6):
            
            cur=words[random.randint(0, len(words)-1)]
           
            
            l=master.guess(cur)
            
            if l==6:
                return
            
            
            newl=[]
            for word in words:
                cnt=0
                for g,c in zip(word, cur):
                    if g == c:
                        cnt += 1
                if cnt==l:
                    newl.append(word)
            
            words=newl