// https://leetcode.com/problems/increasing-triplet-subsequence
// 14 ms

public class Solution {
    public boolean increasingTriplet(int[] nums) {
        Integer cand1 = null, cand2 = null, newCand1 = null;
        
        for(int num : nums) {
            if (cand1 != null && cand2 != null && num > cand2) {
                return true;
            }
            
            if (cand1 == null || (num < cand1 && cand2 == null)) {
                cand1 = num;
            } else if ((num > cand1 && cand2 == null) || (cand2 != null && num < cand2 && num > cand1)) {
                cand2 = num;
            } else if (newCand1 == null) {
                newCand1 = num;
            } else if (num > newCand1 && newCand1 < cand1) {
                cand1 = newCand1;
                cand2 = num;
                newCand1 = null;
            }
        }
        
        return false;
    }
}
