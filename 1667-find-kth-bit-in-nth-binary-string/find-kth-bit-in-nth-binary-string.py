class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        if n==1:
            return "0"
        
        l=(1<<n)
        
        if k<(l//2):
            return self.findKthBit(n-1,k)
        
        elif k==(l//2):
            return "1"
        
        else:
            
            val=self.findKthBit(n-1,l-k)
            
            return "0" if val=="1" else "1"