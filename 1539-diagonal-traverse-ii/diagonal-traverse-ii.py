class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d={}

        for r in range(len(nums)-1,-1,-1):
            for c in range(0,len(nums[r])):
                diag=r+c
                if diag in d:
                    d[diag].append(nums[r][c])
                else:
                    d[diag]=[nums[r][c]]
        print(d)
        res=[]
        key=0
        n=len(nums)-1
        while key in d:
            res.extend(d[key])
            key+=1

        return res
