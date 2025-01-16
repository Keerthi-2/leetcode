class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1)%2==0 and len(nums2)%2==0:
            return 0
        
        res=0
        if  len(nums2)%2:
            for i in nums1:
                res^=i
        
        if  len(nums1)%2:
            for i in nums2:
                res^=i
        
        return res
