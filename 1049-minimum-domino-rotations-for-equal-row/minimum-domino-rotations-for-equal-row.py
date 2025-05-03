class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        val=10**9

        for i in range(1,7):
            cur=i
            top_count=0
            bot_count=0
            valid=True

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
        return val if val!=10**9 else -1
