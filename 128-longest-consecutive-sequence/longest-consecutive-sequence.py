class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        if not nums:
            return 0
        c=1
        k=1
        for num in n:
            if num-1 not in n:
                c=num
                c1=1
                while c+1 in n:
                    c+=1
                    c1+=1
                k=max(c1,k)
        return k