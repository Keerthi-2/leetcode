class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        curra,currb,currc=0,0,0
        total=a+b+c
        
        res=""
        
        for i in range(total):
            if (a>=b and a>=c and curra!=2) or (a>0 and (currb==2 or currc==2)):
                res+="a"
                a-=1
                curra+=1
                currb=0
                currc=0
            elif (b>=a and b>=c and currb!=2) or (b>0 and (curra==2 or currc==2)):
                res+="b"
                b-=1
                currb+=1
                curra=0
                currc=0
            elif (c>=a and c>=b and currc!=2) or (c>0 and (curra==2 or currb==2)):
                res+="c"
                c-=1
                currc+=1
                curra=0
                currb=0
        return res
            