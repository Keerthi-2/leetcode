class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        print(target)
        max_len=-100000
        cur_sum=0
        s=0
        e=len(nums)-1
        f=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
           
            while(s<=i and cur_sum>target):
                cur_sum=cur_sum-nums[s]
                s+=1
            if cur_sum==target:
                f=1
                max_len=max(max_len,i-s+1)
        
        if max_len==-100000:
            return -1
        return len(nums)-max_len
        