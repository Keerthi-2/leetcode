class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res=[]
        
        

        for i in range(len(asteroids)):
            res.append(asteroids[i])
            
            while(len(res)>1 and res[-2]>0 and res[-1]<0):
                first_val=res.pop()
                second_val=res.pop()

                if abs(first_val)<abs(second_val):
                    res.append(second_val)
                elif abs(first_val)>abs(second_val):
                    res.append(first_val)
        
        return res
                
