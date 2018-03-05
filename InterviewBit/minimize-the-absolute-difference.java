// https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/minimize-the-absolute-difference/
// 

public class Solution {
    public int solve(ArrayList<Integer> A, ArrayList<Integer> B, ArrayList<Integer> C) {
        List<List<Integer>> lists = Arrays.asList(A,B,C);
        int[] ind = new int[3];
        
        int minDiff = Integer.MAX_VALUE;
        
        if (A.isEmpty() || B.isEmpty() || C.isEmpty()) return minDiff;
        
        boolean finished = false;

        while(!finished) {
            int i=ind[0], j=ind[1], k=ind[2];
            
            int[]nums = new int[]{A.get(i), B.get(j), C.get(k)};
            
            int min = Arrays.stream(nums).min().getAsInt();
            int max = Arrays.stream(nums).max().getAsInt();
            minDiff = Math.min(minDiff, max-min);
            
            Optional<Integer> minIndex = Arrays.asList(0,1,2).stream().filter(listIndex -> {
                return nums[listIndex] == min && ind[listIndex]+1 < lists.get(listIndex).size();
            }).findFirst();
            
            if (minIndex.isPresent()) {
                ind[minIndex.get()]++;
            } else {
                finished = true;
            }
        }
        
        return minDiff;
    }
}

