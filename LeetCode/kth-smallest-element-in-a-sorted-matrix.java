// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
// 80 ms

public class Solution {
    class Point {
        int i,j;
        
        Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
    
    public int kthSmallest(int[][] matrix, int k) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        
        TreeMap<Integer, LinkedList<Point>> frontier = new TreeMap<>();
        
        for(int col=0; col<matrix[0].length; col++) {
            insert(frontier, matrix, new Point(0, col));
        }
        
        Point current = null;
        
        for(int i=0; i<k; i++) {
            current = poll(frontier);
            
            int row=current.i, col=current.j;

            if(row+1 < matrix[0].length) {
                insert(frontier, matrix, new Point(row+1, col));
            }
        }
        
        return matrix[current.i][current.j];
    }
    
    private void insert(TreeMap<Integer, LinkedList<Point>> frontier, int[][] matrix, Point point) {
        int key = matrix[point.i][point.j];
        
        if(frontier.containsKey(key)) {
            frontier.get(key).add(point);    
        } else {
            frontier.put(key, new LinkedList(Arrays.asList(point)));
        }
    }
    
    private Point poll(TreeMap<Integer, LinkedList<Point>> frontier) {
        LinkedList<Point> points = frontier.get(frontier.firstKey());
        
        Point res = points.pollFirst();
        
        if(points.isEmpty()) {
            frontier.remove(frontier.firstKey());
        }
        
        return res;
    }
}
