class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        cur=arr[0]
        count=1
        n=len(arr)
        for i in range(1,len(arr)):
            if arr[i]==cur:
                count+=1
            else:
                print(cur,count,(count/n)*100)
                if ((count/n)*100)>25:
                    return cur
                cur=arr[i]
                count=1
        
        return cur

