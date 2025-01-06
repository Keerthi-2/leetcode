class Solution:
    def calculateScore(self, s: str) -> int:
        score=0

        d={}

        for i in range(len(s)):
            mirror=chr(122-(ord(s[i])-97))

            if mirror in d:
                if d[mirror]:
                    
                    j=d[mirror].pop()
                    score+=(i-j)
                    continue

            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]]=[i]

        return score


       