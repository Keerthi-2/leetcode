class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a=1
        e=1
        i=1
        o=1
        u=1
        MOD=(10**9)+7
        for k in range(1,n):
            a_next=e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a
            
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        
        return (a + e + i + o + u) % MOD



        