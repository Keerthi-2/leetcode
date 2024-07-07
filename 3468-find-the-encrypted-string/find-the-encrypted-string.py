class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        k=k%n
        res=s[k:]+s[:k]

        return res