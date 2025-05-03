class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        val=10**9

        def minrotations(input):
            cur=input
            top_count=0
            bot_count=0
            valid=True
            val=10**9
            for t,b in zip(tops,bottoms):
                if t!=cur and b!=cur:
                    valid=False
                    break
                
                if t!=cur:
                    top_count+=1
                if b!=cur:
                    bot_count+=1

            if valid:
                val=min(val,top_count,bot_count)
            return val
        ans=min(minrotations(tops[0]),minrotations(bottoms[0]))
        return ans if ans!=10**9 else -1
