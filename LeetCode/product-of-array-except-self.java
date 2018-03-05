// https://leetcode.com/problems/product-of-array-except-self
// 4 ms

public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        
        for(int i=result.length-1; i>=0; i--){
            int last = i+1<result.length ? result[i+1] : 1;
            result[i] = nums[i]*last; 
        }
        
        for(int i=0; i<nums.length; i++){
            int last = i>0 ? nums[i-1] : 1;
            nums[i] = nums[i]*last; 
        }
        
        for(int i=0; i<nums.length; i++){
            int leftMult = i>0 ? nums[i-1] : 1;
            int rightMult = i+1<result.length ? result[i+1] : 1;
            result[i] = leftMult * rightMult; 
        }
        
        return result;
    }
}
