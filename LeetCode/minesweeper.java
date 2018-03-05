// https://leetcode.com/problems/minesweeper
// 12 ms

public class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        if(board[click[0]][click[1]]=='M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }
        
        Deque<int[]> queue = new LinkedList<>();
        queue.add(click);
        
        while(!queue.isEmpty()) {
            int[] point = queue.pollFirst();
            int i=point[0], j=point[1];
            
            int minesAround = 0;
            List<int[]> potentialPoints = new LinkedList<>();
            
            for(int di=-1; di<=1; di++) {
                for(int dj=-1; dj<=1; dj++) {
                    int ni=i+di, nj=j+dj;
                    if(ni<0 || ni>=board.length || nj<0 || nj>=board[0].length || (ni==i && nj==j)) continue;
                    
                    if(board[ni][nj] == 'M') minesAround++;
                    if(board[ni][nj] == 'E') potentialPoints.add(new int[]{ni, nj});
                }
            }

            board[i][j] = minesAround == 0 ? 'B' : Character.forDigit(minesAround, 10);
            
            if(minesAround == 0) {
                for(int[] p:potentialPoints) {
                    board[p[0]][p[1]] = 'V';
                    queue.add(p);
                }
            }
        }
        
        return board;
    }
}
