// https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/length-of-longest-subsequence/
// 

public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public int longestSubsequenceLength(final List<Integer> A) {
        int[] lis = longestSubsequences(A, true);
        int[] lds = longestSubsequences(A, false);
        
        int longest = 0;
        
        for(int i=0; i<A.size(); i++) {
            int current = lis[i] + lds[i] - 1;
            longest = Math.max(current, longest);
        }
        
        return longest;
    }
    
    private int[] longestSubsequences(final List<Integer> A, boolean increasing) {
        int[] result = new int[A.size()];
        Arrays.fill(result, 1);
        
        for(int ii=0; ii<A.size(); ii++) {
            for(int jj=0; jj<ii; jj++) {
                
                int i = increasing ? ii : A.size()-1-ii;
                int j = increasing ? jj : A.size()-1-jj;
                
                if(A.get(j) < A.get(i)) {
                    result[i] = Math.max(result[j]+1, result[i]);
                }
            }
        }
        
        return result;
    }
}

