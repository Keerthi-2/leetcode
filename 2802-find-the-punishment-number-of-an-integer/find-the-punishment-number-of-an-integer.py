class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(t,ind):

            if ind==len(s):
                if t==0:
                    self.valid=True
                return 
            for i in range(ind+1,len(s)+1):
                left,right=int(s[ind:i]),(s[i:])
                print(left,right)
                if left<=t:
                    backtrack(t-left,i)




        res=0

        for i in range(1,n+1):
            self.valid=False
            s=str(i*i)
            backtrack(i,0)
            if self.valid:
              
                res+=i*i
        return res
        