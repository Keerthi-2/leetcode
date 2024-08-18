from heapq import heapify
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
       # 2 4 6  3 6 9
    
        l=[1]
        heapify(l)
        s=set()
        # two=2
        # thr=3
        # five=5
        while(n>0):
            
            cur=heappop(l)
            print(cur)
            
            if cur*2 not in s:
                heappush(l,cur*2)
                s.add(cur*2)
            if cur*3 not in s:
                heappush(l,cur*3)
                s.add(cur*3)
            if cur*5 not in s:
                heappush(l,cur*5)
                s.add(cur*5)
            
            
            
            n-=1
            
            if n==0:
                return cur
        
        
        return -1
            
        
        
        
        
        
        