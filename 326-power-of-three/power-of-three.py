class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        
        if n==1:
            return True
        if n!=1 and n%3!=0:
            return False
        
        
        if (self.isPowerOfThree(n//3)==False):
            return False
        else: return True
        