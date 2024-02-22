class Solution:
    def isValid(self, s: str) -> bool:

        while("abc" in s):
            s=s.replace('abc','')

        if len(s)>0:
            return False
        return True
        