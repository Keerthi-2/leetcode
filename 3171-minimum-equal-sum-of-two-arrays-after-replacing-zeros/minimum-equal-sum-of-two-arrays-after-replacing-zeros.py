class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        z1=0
        z2=0
        s1=0
        s2=0

        for i in nums1:
            if i==0:
                z1+=1
            s1+=max(1,i)
        
        for i in nums2:
            if i==0:
                z2+=1
            s2+=max(1,i)
        
        if (z1==0 and s1<s2) or (z2==0 and s2<s1): return -1

        return max(s1,s2)