class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s = "ADOBECODEBANC", t = "ABC"
        mt = {}
        n = len(t)
        for i in range(n):
            if t[i] in mt:
                mt[t[i]] += 1
            else:
                mt[t[i]] = 1
        # A-  1
        # B - 1
        # C - 1
        distinct = len(mt)
        i=0
        end=-1
        start=-1
        minlength=100000
        for j in range(len(s)):
            
            if s[j] in mt:
                mt[s[j]]-= 1
                if mt[s[j]] == 0: distinct -= 1
            while distinct == 0:

                if (j-i+1)<minlength:
                    minlength = (j-i+1)
                    start=i
                    end=j
                if s[i] in mt: 
                    mt[s[i]] += 1
                    if mt[s[i]] == 1 : distinct += 1
                
                i+=1;
            
        ans = ""
    
        return s[start:end+1]
        