// https://leetcode.com/problems/array-nesting
// 40 ms

public class Solution {
    public int arrayNesting(int[] nums) {
        int[] memo = new int[nums.length];
        
        int largestSet = 0;
        
        for(int i=0; i<nums.length; i++) {
            largestSet = Math.max(largestSet, longestSetFromI(nums, memo, i));
        }
        
        return largestSet;
    }
    
    private int longestSetFromI(int[] nums, int[] memo, int i) {
        if(memo[i] > 0) return memo[i];
        
        int count=0;
        int j=i;
        
        do {
            count++;    
            j=nums[j];
        } while(j != i);
        
        j=i;
        do {
            memo[j]=count;
            j=nums[j];
        } while(j != i);
        
        return count;
    }
}
