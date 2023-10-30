class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        res=[]

        for i in arr:
            cur=i
            count=0
            while(cur!=0):
                count+=cur%2
                cur=cur//2
            res.append([count,i])
        res.sort()
        print(res)
        ans=[]
        ans=[res[i][1] for i in range(len(res))]
        return ans
        