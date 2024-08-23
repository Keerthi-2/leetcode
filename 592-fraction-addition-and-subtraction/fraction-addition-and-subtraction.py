class Solution:
    def fractionAddition(self, exp: str) -> str:
        
        num=0
        denom=1
        
        
        i=0
        n=len(exp)
        
        while(i<n):
            cur_num=0
            cur_denom=0
            
            isneg=False
            
            if exp[i]=='-' or exp[i]=='+':
                if exp[i]=='-':
                    isneg=True
                
                i+=1
            
            while(i<len(exp) and exp[i].isdigit()):
                val=int(exp[i])
                cur_num=cur_num*10+val

                i+=1
                
            if isneg:
                cur_num *= -1
            
            i+=1
            
            while(i<len(exp) and exp[i].isdigit()):
                vald=int(exp[i])
                cur_denom=cur_denom*10+vald
                i+=1
            
            num=cur_num*denom+num*cur_denom
            denom=denom*cur_denom
            print(num,denom)
            
        gcd = abs(self._find_gcd(num, denom))

        # reduce fractions
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"

    def _find_gcd(self, a, b):
        if a == 0:
            return b
        return self._find_gcd(b % a, a)
        
    
                
            
            