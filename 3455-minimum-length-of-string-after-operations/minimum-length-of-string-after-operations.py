class Solution:
    def minimumLength(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1

        l=len(s)
        print(l,d)
        for k,v in d.items():
            if v>=3:
                if v%2==0:
                    l=l-(v-2)
                else:
                    l=l-(v-1)
              
        
        return l


      #  3-1 4-2 5-1 6-2 7-1 8-2 9-1
        
