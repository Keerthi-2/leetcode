class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def helper(r,b):
            h=0
            i=1
            
            for i in range(1,50):
                if i%2==1:
                    if r>=i:
                        r-=i
                    else:
                        break
                else:
                    if b>=i:
                        b-=i
                    else:
                        break
                h+=1
            
            return h
                
        return max(helper(red,blue),helper(blue,red))