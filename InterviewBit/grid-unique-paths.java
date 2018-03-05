// https://www.interviewbit.com/courses/programming/topics/math/problems/grid-unique-paths/
// 

import java.math.BigInteger;

public class Solution {
    public int uniquePaths(int a, int b) {
        int pascalsRow = (Math.max(a,b)+Math.min(a,b)-1)-1;
        int pascalsColumn = Math.min(a,b)-1;
        
        return nChooseK(pascalsRow, pascalsColumn).intValue();
    }
    
    private BigInteger nChooseK(int n, int k) {
        BigInteger result = BigInteger.ONE;
        for (int i=0; i<k; i++) {
            result = result.multiply(BigInteger.valueOf(n-i)).divide(BigInteger.valueOf(i+1));
        }
        return result;
    }
}

