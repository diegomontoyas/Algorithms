// https://leetcode.com/problems/house-robber
// 1 ms

public class Solution {
    public int rob(int[] nums) {
        return maxProfit(0, nums, new int[nums.length]);
    }
    
    private int maxProfit(int i, int[] nums, int[] memo) {
        while(i<nums.length && nums[i]==0) i++;
        
        if(i >= nums.length) return 0;
        if(i == nums.length-1) return nums[i];
        if(memo[i]>0) return memo[i];
        
        
        memo[i] = Math.max(nums[i] + maxProfit(i+2, nums, memo), nums[i+1] + maxProfit(i+3, nums, memo));
        return memo[i];
    }
}
