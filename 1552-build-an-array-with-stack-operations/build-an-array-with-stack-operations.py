class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res=[]
        k=0
        length=len(target)
        
        i=1
        ind=0
        while(i<=n and ind<length):
            if i!=target[ind]:
                res.append("Push")
                res.append("Pop")

            else:
                res.append("Push")
                ind+=1




            i+=1

        return res
            
