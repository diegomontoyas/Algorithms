// https://leetcode.com/problems/shortest-unsorted-continuous-subarray
// 34 ms

public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int lowerL=-1;
        Integer swappedNum=null;
        
        for(int i=1; i<nums.length; i++) {
            if(nums[i] < nums[i-1]){
                
                if(lowerL == -1) {
                    int j=i;
                    while(j>0 && nums[j-1] > nums[i]) j--;
                    lowerL=j;
                    swappedNum = nums[i];
                } else if(nums[i] < swappedNum) {
                    while(lowerL>0 && nums[lowerL-1] > nums[i]) lowerL--;
                    swappedNum = nums[i];
                }
            }
        }
        
        int upperL=-1;

        for(int i=nums.length-2; i>=0; i--) {
            if(nums[i] > nums[i+1]){
                
                if(upperL == -1) {
                    int j=i;
                    while(j<nums.length-1 && nums[j+1] < nums[i]) j++;
                    upperL=j+1;
                    swappedNum = nums[i];
                } else if(nums[i] > swappedNum) {
                    while(upperL<nums.length && nums[upperL] < nums[i]) upperL++;
                    swappedNum = nums[i];
                }
            }
        }
        
        System.out.println(lowerL+":"+upperL);
        return upperL-lowerL;
    }
}
