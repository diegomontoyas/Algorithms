// https://leetcode.com/problems/move-zeroes
// 21 ms

public class Solution {
    public void moveZeroes(int[] nums) {
        
        int i=0;
        while (i<nums.length) {
            while (i < nums.length && nums[i] != 0) {
                i++;
            } 
            
            if (i < nums.length) {
                int j=i+1;
                while (j < nums.length && nums[j] == 0) {
                    j++;
                }
                
                if (j == nums.length) return;
                nums[i] = nums[j];
                nums[j] = 0;
                i++;
            }
        }
    }
}
