class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        res1=[]

        for i in range(len(l)):
            a=l[i]
            b=r[i]

            cur=[]
            for j in range(a,b+1):
                cur.append(nums[j])
            cur.sort()
            ans=0
            length=len(cur)-1
          
            p=cur[1]-cur[0]
            j=1
            while(j<len(cur) and (cur[j]-cur[j-1])==p):
                j+=1
                # res+=1
                # if res>1:
                #     ans=max(ans,res)
            
            j=j-1
           
            if j==len(cur)-1:
                res1.append(True)
            else:
                res1.append(False)
        return res1
                

        