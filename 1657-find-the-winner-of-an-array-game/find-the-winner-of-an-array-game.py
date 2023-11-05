class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur=arr[0]
        winstreak=0
        m=max(arr)
        for i in range(1,len(arr)):
            opp=arr[i]
            if cur>opp:
                winstreak+=1
            else:
                winstreak=1
                cur=opp
            if winstreak==k or m==cur:
                return cur
        
        
        