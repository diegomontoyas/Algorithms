// https://leetcode.com/problems/friend-circles
// 27 ms

public class Solution {
    public int findCircleNum(int[][] M) {
        BitSet visited = new BitSet(M.length);
        int circles = 0;
        
        for(int f=0; f<M.length; f++){
            if(visited.get(f)) continue;
            circles++;
            
            Deque<Integer> queue = new LinkedList<Integer>();
            queue.add(f);
            visited.set(f);
            
            while(!queue.isEmpty()) {
                int current = queue.pollFirst();
                
                for(int j=0; j<M.length; j++) {
                    if(M[current][j]==1 && !visited.get(j)) {
                        queue.add(j);
                        visited.set(j);
                    }
                }
            }
        }
        
        return circles;
    }
}
