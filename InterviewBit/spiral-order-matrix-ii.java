// https://www.interviewbit.com/courses/programming/topics/arrays/problems/spiral-order-matrix-ii/
// 

public class Solution {
    public ArrayList<ArrayList<Integer>> generateMatrix(int a) {
        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();
        
        for (int i=0; i<a; i++) {
            matrix.add(new ArrayList<>(Collections.nCopies(a, 0)));
        }
        
        int num = 1;
        
        for(int d=0; d<Math.ceil(a/2.0); d++) {
            
            //Set top row
            for(int j=d; j<a-1-d; j++) {
                matrix.get(d).set(j, num++);
            }
            
            //Set right column
            for(int i=d; i<a-1-d; i++) {
                matrix.get(i).set(a-1-d, num++);
            }

            //Set bottom row
            for(int j=a-1-d; j>d; j--) {
                matrix.get(a-1-d).set(j, num++);
            }
            
            //Set left column
            for(int i=a-1-d; i>d; i--) {
                matrix.get(i).set(d, num++);
            }
        }
        
        if (a%2!=0) matrix.get(a/2).set(a/2, num);
        return matrix;
    }
}

