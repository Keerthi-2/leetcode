class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m=0
        chunk=0
        s=[]
        m=0
        for i in range(0,len(arr)):
            #s.append(arr[i])
            m=arr[i]
            while(len(s)>0 and s[-1]>arr[i]):
                m=max(m,s[-1])
                s.pop()
            s.append(m)

            
        
        return len(s)

            
        