// https://www.interviewbit.com/courses/programming/topics/arrays/problems/max-sum-contiguous-subarray/
// 

public class Solution {
    // DO NOT MODFIY THE LIST. 
    public int maxSubArray(final List<Integer> a) {
        int max = a.get(0);
        int[] sum = new int[a.size()];
        sum[0] = a.get(0);
 
        for (int i = 1; i < a.size(); i++) {
            sum[i] = Math.max(a.get(i), sum[i - 1] + a.get(i));
            max = Math.max(max, sum[i]);
        }
 
        return max;
    }
}

