class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(x,n):
            if n==0:
                return 1
        
            halfpower=power(x,n//2)
            if n%2>0:
                
                return x*halfpower*halfpower
            else:
                return halfpower*halfpower

        if n<0:
            n=n*-1
            return 1/(power(x,n))
        return power(x,n)
