// https://leetcode.com/problems/out-of-boundary-paths
// 100 ms

import java.math.BigInteger;

public class Solution {
    public int findPaths(int m, int n, int N, int i, int j) {
        return findPaths(m, n, N, i, j, new HashMap<>()).mod(BigInteger.valueOf((long)Math.pow(10, 9)+7)).intValue();
    }
    
    private BigInteger findPaths(int m, int n, int movesLeft, int i, int j, HashMap<String, BigInteger> memo) {
        if(i<0 || j<0 || i>=m || j>=n || movesLeft<=0) return BigInteger.ZERO;
        
        String memoKey = i+":"+j+":"+movesLeft;
        
        if(memo.containsKey(memoKey)) {
            return memo.get(memoKey);
        }
        
        BigInteger count = BigInteger.ZERO;
        
        if(i-1 < 0) count = count.add(BigInteger.ONE);
        if(i+1 >= m) count = count.add(BigInteger.ONE);
        if(j-1 < 0) count = count.add(BigInteger.ONE);
        if(j+1 >= n) count = count.add(BigInteger.ONE);
        
        count = count.add(findPaths(m, n, movesLeft-1, i-1, j, memo));
        count = count.add(findPaths(m, n, movesLeft-1, i+1, j, memo));
        count = count.add(findPaths(m, n, movesLeft-1, i, j-1, memo));
        count = count.add(findPaths(m, n, movesLeft-1, i, j+1, memo));
        
        memo.put(memoKey, count);
        return count;
    }
}
