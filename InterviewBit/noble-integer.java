// https://www.interviewbit.com/courses/programming/topics/arrays/problems/noble-integer/
// 

public class Solution {
    public int solve(ArrayList<Integer> A) {
        A.sort(Integer::compareTo);
        
        for(int i=0; i<A.size(); i++) {
            if (A.get(i) == A.size()-1-i && (i==A.size()-1 || A.get(i+1) != A.get(i))) return 1;
        }
        
        return -1;
    }
}

