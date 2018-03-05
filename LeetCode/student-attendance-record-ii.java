// https://leetcode.com/problems/student-attendance-record-ii
// 511 ms

public class Solution {
    public int checkRecord(int N) {
        if(N==0) return 1;
        
        int[][][] memo = new int[N][2][3];
        memo[0]=new int[][]{{3,3,2},{2,2,1}};
        
        for(int n=1; n<N; n++) {
            for(int a=0; a<2; a++) {
                for(int l=0; l<3; l++) {
                    long puttingA = a==0 ? memo[n-1][a+1][0] : 0;
                    long puttingL = l<2 ? memo[n-1][a][l+1] : 0;
                    long puttingP = memo[n-1][a][0];
                    
                    memo[n][a][l] = (int)((puttingA + puttingL + puttingP)%1000000007);
                }
            }
        }
        
        return memo[N-1][0][0];
    }
}
