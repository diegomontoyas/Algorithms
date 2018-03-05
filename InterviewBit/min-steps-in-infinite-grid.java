// https://www.interviewbit.com/courses/programming/topics/arrays/problems/min-steps-in-infinite-grid/
// 

public class Solution {
    // X and Y co-ordinates of the points in order.
    // Each point is represented by (X.get(i), Y.get(i))
    public int coverPoints(ArrayList<Integer> X, ArrayList<Integer> Y)
    {
        int n=0;
        
        for (int i=0; i<X.size()-1; i++)
        {
            n += Integer.max(Math.abs(X.get(i+1)-X.get(i)), Math.abs(Y.get(i+1)-Y.get(i)));
        }
        
        return n;
    }
}

