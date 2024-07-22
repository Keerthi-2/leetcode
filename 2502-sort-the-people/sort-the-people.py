class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        group=[]
        res=[]
        
        for i in range(len(names)):
            group.append([heights[i],names[i]])
        
        group.sort(reverse=True)
        
        for i in group:
            res.append(i[1])
        
        return res