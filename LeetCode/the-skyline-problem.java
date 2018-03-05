// https://leetcode.com/problems/the-skyline-problem
// 157 ms

public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        TreeMap<Integer, Integer> heap = new TreeMap<>();
        heap.put(0, 1);
        
        int[][] points = unwind(buildings);
        ArrayList<int[]> result = new ArrayList<>();
        
        System.out.println(Arrays.deepToString(points));

        for(int i=0; i<points.length; i++) {
            int[] point = points[i];
            int x = point[0];
            int height = point[1];
            boolean buildingBeginning = point[2] == 1;
            height = Math.abs(height);
            
            int lastMaxHeight = heap.lastKey();
            
            if(buildingBeginning) {
                if(!heap.containsKey(height)) {
                    heap.put(height, 1);
                } else {
                    heap.put(height, heap.get(height)+1);
                }
                
            } else {
                if(heap.get(height) > 1) { 
                    heap.put(height, heap.get(height)-1);
                } else {
                    heap.remove(height);
                }
            }
        
            int newHeight = heap.lastKey();
            
            if(heap.lastKey() != lastMaxHeight) {
                result.add(new int[]{x, newHeight});
            }
        }
        
        return result;
    }

    private int[][] unwind(int[][] buildings) {
        
        int[][] result = new int[buildings.length*2][3];
        
        int i=0;
        for(int[] building : buildings) {
            result[i] = new int[]{building[0], building[2], 1};
            result[i+1] = new int[]{building[1], building[2], -1};
            i+=2;
        }
        
        Arrays.sort(result, (l,r) -> {
            int xComp = Integer.compare(l[0], r[0]);
            if(xComp != 0) return xComp;
            
            if(l[2] == r[2] && l[2] == 1) {
                return -Integer.compare(l[1], r[1]);
                
            } else if(l[2] == r[2] && l[2] == -1) {
                return Integer.compare(l[1], r[1]);
                
            } else if(l[2] == -1){
                return 1; 
            } else {
                return -1;
            }
        });
        
        return result;
    }
}
