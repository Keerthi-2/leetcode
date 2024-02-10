class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #For Odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res +=1
                l -= 1
                r += 1
            #For Even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res +=1
                l -= 1
                r += 1
        return res
        