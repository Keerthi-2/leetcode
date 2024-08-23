class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        pref=[0]*102
        
        for cur in ranges:
            pref[cur[0]]+=1
            pref[cur[1]+1]-=1
        
        for i in range(1,len(pref)):
            pref[i]+=pref[i-1]
        
        for i in range(left,right+1):
            if pref[i]<=0:
                return False
    
        return True