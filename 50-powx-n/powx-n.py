class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n=n*-1
            return 1/(self.myPow(x,n))
        
        if n==0:
            return 1
    
        halfpower=self.myPow(x,n//2)
        if n%2>0:
            
            return x*halfpower*halfpower
        else:
            return halfpower*halfpower

        
        
