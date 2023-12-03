class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(i, target):
            # Given a string s and int target, return True if s can be partitioned into contiguous substrings s.t. sum of the integer
            # values of the substrings equals target.
            # Backtrack pruning: don't need to consider splitting if splitting results in some number > target
            
            if i == len(s):
                if target == 0:
                    self.valid = True
                return
            
            for j in range(i + 1, len(s) + 1):
                # try to partition s[:j] and s[j:]
                left, right = s[i:j], s[i + j:]
                if int(left) <= target:
                    backtrack(j, target - int(left))
        
        res = 0
        for i in range(1, n + 1):
            self.valid = False
            s = str(i * i)
            backtrack(0, i)
            if self.valid:
                res += i * i
        
        return res