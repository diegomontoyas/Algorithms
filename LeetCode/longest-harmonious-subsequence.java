// https://leetcode.com/problems/longest-harmonious-subsequence
// 56 ms

public class Solution {
    public int findLHS(int[] nums) {
        Arrays.sort(nums);
        
        int longest=0;
        int i=0, j=0;
        
        while(i<nums.length && j<nums.length) {
            int diff = nums[j]-nums[i];
            
            if(diff <= 1) {
                if(diff == 1 && j-i+1 > longest) longest = j-i+1;
                j++;
            } else {
                i++;
            }
        }
        
        return longest;
    }
}
