class Solution:
    def sortedSquares(self,arr: List[int]) -> List[int]:
        def binarysearch(arr,l,h):
            while(l<=h):
                mid=(l+h)//2
                if arr[mid]<0:
                    l=mid+1
                else:
                    h=mid-1
            return h
        res=[]
        n=len(arr)
        cur=binarysearch(arr,0,n-1)
        print(cur)

        j=cur
        cur+=1

        while(j>=0 and cur<n):
            if arr[j]*arr[j]<=arr[cur]*arr[cur]:
                res.append(arr[j]*arr[j])
                j-=1
            else:
                res.append(arr[cur]*arr[cur])
                cur+=1
        
        while(j>=0):
            res.append(arr[j]*arr[j])
            j-=1
        while(cur<n):
            res.append(arr[cur]*arr[cur])
            cur+=1
        
        return res
