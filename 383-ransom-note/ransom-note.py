class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      
        l=[0]*26
        
        for i in magazine:
            ind=ord(i)-97
            l[ind]+=1
        
        for i in ransomNote:
            ind=ord(i)-97
            l[ind]-=1
            if l[ind]<0:
                return False
        
        return True