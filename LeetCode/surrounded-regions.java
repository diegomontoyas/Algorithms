// https://leetcode.com/problems/surrounded-regions
// 125 ms

public class Solution {
    class Point {
        int row, col;
        Point(int row, int col) {this.row = row; this.col = col;}
    }
    
    public void solve(char[][] board) {
        if(board.length == 0 || board[0].length == 0) return;
        
        boolean[][] explored = new boolean[board.length][board[0].length];
        
        for(int row=0; row<board.length; row++) {
            for(int col=0; col<board[row].length; col++) {
                
                if (board[row][col] == 'O' && !explored[row][col]) {
                    tryCaptureRegion(board, explored, new Point(row, col));
                }
            }
        }
    }
    
    private void tryCaptureRegion(char[][] board, boolean[][] explored, Point startPoint) {
        HashMap<String, Point> visited = new HashMap<>();
        visited.put(startPoint.row+":"+startPoint.col, startPoint);
        
        Deque<Point> queue = new LinkedList<Point>();
        queue.add(startPoint);
        
        while(!queue.isEmpty()) {
            Point p = queue.pollFirst();
            int row = p.row, col = p.col;
            
            explored[row][col] = true;
            
            if(row==0 || col==0 || row==board.length-1 || col==board[0].length-1) return;
            
            List<Point> neighbors = Arrays.asList(new Point(row-1, col), new Point(row+1, col), 
                                                  new Point(row, col-1), new Point(row, col+1));
            
            for (Point neighbor : neighbors) {
                int nRow = neighbor.row, nCol = neighbor.col;
                String key = nRow+":"+nCol;
                
                if(board[nRow][nCol] == 'O' && !visited.containsKey(key)) {
                    visited.put(key, neighbor);
                    queue.add(neighbor);
                }
            }
        }
        
        for (Point toCapture : visited.values()) {
            board[toCapture.row][toCapture.col] = 'X';
        }
    }
}
