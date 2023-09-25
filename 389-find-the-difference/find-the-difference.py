class Solution:
    def findTheDifference(dlf, s: str, t: str) -> str:
        if len(s)==0:
            return t
        xor=0
        for i in s:
            xor=xor^ord(i)
        for i in t:
            xor=xor^ord(i)
        return chr(xor)


        