// https://leetcode.com/problems/shuffle-an-array
// 281 ms

import java.util.concurrent.ThreadLocalRandom;

public class Solution {

    private int[] original;
    private int[] indices;

    public Solution(int[] nums) {
        original = nums;
        indices = IntStream.range(0, nums.length).toArray();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int[] shuffled = new int[original.length];
        
        for(int i=0; i<original.length; i++){
            int randomIndexIndex = ThreadLocalRandom.current().nextInt(0, indices.length-i);
            int randomIndex = indices[randomIndexIndex];
            indices[randomIndexIndex] = indices[indices.length-1-i];
            indices[indices.length-1-i] = randomIndex;
            
            shuffled[randomIndex] = original[i];
        }
        
        return shuffled;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
