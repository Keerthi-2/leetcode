class Solution:
    def finalString(self, s: str) -> str:
        # process from the right end, write from both ends
        n = len(s)
        result = [""]*n
        left, right = 0, n-1
        parity = 1
        for i in range(n-1,-1,-1):
            l = s[i]
            if l == "i": 
                parity = 1 - parity
            elif parity == 1:
                result[right] = l
                right -= 1
            else:
                result[left] = l
                left += 1
        return "".join(result)