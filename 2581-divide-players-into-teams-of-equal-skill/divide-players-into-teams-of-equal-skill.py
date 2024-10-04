class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        print(skill)
        i=0
        j=len(skill)-1
        
        val=skill[i]+skill[j]
        
        ans=skill[i]*skill[j]
        
        i+=1
        j-=1
        while(i<j):
            print(val,skill[i]*skill[j])
            if val!=(skill[i]+skill[j]):
                return -1
            ans+=(skill[i]*skill[j])
            i+=1
            j-=1
        
        return ans