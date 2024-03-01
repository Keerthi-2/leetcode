class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res=''
        ones=0
        n=len(s)

        for i in s:
            if i=='1':
                ones+=1
        z=n-ones
        print(ones,z,n)
        res='1'*(ones-1)+'0'*(z)+'1'

        return res
        