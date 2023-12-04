class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res=float('-inf')

        ans=""
        n=len(num)
        for i in range(0,n-2):
            if int(num[i])==int(num[i+1])==int(num[i+2]):
                val=int(num[i:i+3])
                if val>res:

                    res=max(res,val)
                    ans=num[i:i+3]
            
        return ans
        