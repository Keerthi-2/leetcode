import java.lang.*;
class Solution {
    public int maxFrequency(int[] nums, int k) {
        long cur=0;
        int res=0;
        int left=0;
        Arrays.sort(nums);
        for(int right=0;right<nums.length;right+=1){
            cur+=nums[right];
            int target=nums[right];
            while(((right-left+1)*target)-cur>k){
                cur-=nums[left];
                left+=1;
            }
            res=Math.max(res,right-left+1);
        }
        return res;
    }
}