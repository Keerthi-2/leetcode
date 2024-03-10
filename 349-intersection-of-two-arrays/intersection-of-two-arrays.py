class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        

        s=set()
        ans=[]
        print(nums1,nums2)
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                print(i)
                i+=1
            elif nums1[i]>nums2[j]:
                print(i)
                j+=1
            else:
                print("equal")
                s.add(nums1[i])
                i+=1
                j+=1
        print(s)
        return list(s)
            