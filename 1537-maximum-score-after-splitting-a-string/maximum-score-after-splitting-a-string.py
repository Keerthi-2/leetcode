class Solution:
    def maxScore(self, s: str) -> int:

        res=0
        t=s.count('1')
        zeroes=0
        ones=0
        print(t)
        for i in range(len(s)):
            
            print(zeroes,ones)
            if zeroes==0 or t-ones==0:
                res=max(res,zeroes+(t-ones)-1)
            else:
                res=max(res,zeroes+(t-ones))
            if s[i]=='0':
                zeroes+=1
            else:
                ones+=1
        if zeroes==0 or t-ones==0:
            res=max(res,zeroes+(t-ones)-1)
        else:
            res=max(res,zeroes+(t-ones))
        
        return res

        