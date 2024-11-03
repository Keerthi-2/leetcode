class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n=s+s
        l=len(s)
        for i in range(len(s)):
            if n[i:i+l]==goal:
                return True
        
        return False