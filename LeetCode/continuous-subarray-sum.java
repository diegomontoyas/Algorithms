// https://leetcode.com/problems/continuous-subarray-sum
// 76 ms

public class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        
        for(int i=0; i<nums.length; i++) {
            int currentSum = 0;
            
            for(int j=i; j<nums.length; j++) {
                currentSum += nums[j];
                if(j-i>0 && ((k==0 && currentSum==0) || (k!=0 && currentSum % k == 0))) return true;
            }
        }
        
        return false;
    }
}
