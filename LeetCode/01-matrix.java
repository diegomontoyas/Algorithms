// https://leetcode.com/problems/01-matrix
// 42 ms

public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        _prepareMatrix(matrix);
        Deque<int[]> queue = _buildInitialQueue(matrix);
        
        while(!queue.isEmpty()) {
            int[] current = queue.pollFirst();
            int i=current[0], j=current[1];
            _addNeighborsToQueue(matrix, queue, i, j);
        }
        
        return matrix;
    }
    
    private Deque<int[]> _buildInitialQueue(int[][] matrix) {
        Deque<int[]> queue = new LinkedList<>();
        
        for(int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[0].length; j++) {
                if(matrix[i][j] == 0) {
                    _addNeighborsToQueue(matrix, queue, i, j);
                }
            }
        }

        return queue;
    }
    
    private void _addNeighborsToQueue(int[][] matrix, Deque<int[]> queue, int i, int j) {
        for(int[] point : new int[][]{{-1,0},{1,0},{0,-1},{0,1}}) {
            int newi = i+point[0], newj = j+point[1];
            if(newi<0 || newi>=matrix.length || newj<0 || newj >= matrix[0].length) continue;
            if(matrix[newi][newj]!=-1) continue;
            matrix[newi][newj] = matrix[i][j]+1;
            queue.add(new int[]{newi, newj});
        }
    }
    
    private void _prepareMatrix(int[][] matrix) {
        for(int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[0].length; j++) {
                if(matrix[i][j] == 1) matrix[i][j] = -1;
            }
        }
    }
}
