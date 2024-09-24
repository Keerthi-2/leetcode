class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        hs=set()

        for i in arr1:
            cur=str(i)
            s=''
            for j in range(len(cur)):
                s+=cur[j]
                hs.add(s)
        
        print(s)
        ans=0
        for i in arr2:
            cur=''
            st=str(i)
            for j in st:
                cur+=j
                if cur in hs:
                    ans=max(ans,len(cur))

        return ans