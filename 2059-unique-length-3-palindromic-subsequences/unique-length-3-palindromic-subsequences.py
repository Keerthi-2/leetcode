class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(map(lambda i: len(set(s[s.index(i)+1:s.rindex(i)])), set(s)))