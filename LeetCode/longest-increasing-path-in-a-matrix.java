// https://leetcode.com/problems/longest-increasing-path-in-a-matrix
// 202 ms

public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int max = 0;
        HashMap<String, Integer> cache = new HashMap<>();

        for (int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[i].length; j++) {
                int length = longestIncreasingPath(matrix, i, j, cache);
                max = Math.max(length, max);
            }
        }

        return max;
    }

    private int longestIncreasingPath(int[][] matrix, int i, int j, HashMap<String, Integer> cache) {
        
        String cacheKey = i+":"+j;
        if(cache.containsKey(cacheKey)) return cache.get(cacheKey);
        
        int longestFromHere = 0;

        for (int[] point : new int[][]{{i+1,j}, {i-1,j}, {i,j+1}, {i, j-1}}) {
            int newi=point[0], newj=point[1];
            String pointString = newi+":"+newj;

            if(newi>=0 && newi<matrix.length && newj>=0 && newj<matrix[0].length
            && matrix[newi][newj] > matrix[i][j]) {
                longestFromHere = Math.max(longestFromHere, longestIncreasingPath(matrix, newi, newj, cache));
            }
        }
        
        cache.put(cacheKey, longestFromHere+1);
        return longestFromHere+1;
    }
}
