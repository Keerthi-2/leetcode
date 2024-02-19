class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n!=0:
            
            if n&(n-1)==0:
                return True
            

        return False
        