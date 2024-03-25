class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        if len(set(cards))==len(cards):
            return -1
        d={}
        i=0
        j=0
        ans=10000000
        while(j<len(cards)):

            if cards[j] in d:
                if ans>(j-d[cards[j]]):
                    ans=j-d[cards[j]]
                d[cards[j]]=j
            else:
                d[cards[j]]=j
            j+=1
        
        return ans+1
