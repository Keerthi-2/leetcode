from collections import Counter
from heapq import heapify,heappush,heappop
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        l=[]
        for k,v in d.items():
            heappush(l,(-v,k))
        res=''
        while(l):
            freq,key=heappop(l)
            freq=freq*-1
            res+=(key)*(freq)
        
        return res
        