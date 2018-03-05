// https://leetcode.com/problems/brick-wall
// 31 ms

public class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int maxSpacesCrossed = 0; 
        HashMap<Integer, Integer> spaceAtIndexCounts = new HashMap<>();
        
        for(List<Integer> row : wall) {
            int currentSpace = 0;
            
            for(int i=0; i<row.size()-1; i++) {
                Integer brickLength = row.get(i);
                currentSpace += brickLength;
                maxSpacesCrossed = Math.max(maxSpacesCrossed, increment(spaceAtIndexCounts, currentSpace));
            }
        }
        
        return wall.size()-maxSpacesCrossed;
    }
    
    private Integer increment(HashMap<Integer, Integer> map, Integer key) {
        if(map.containsKey(key)) {
            Integer currentCount = map.get(key);
            map.put(key, currentCount+1);
            return currentCount+1;
        } else {
            map.put(key, 1);
            return 1;
        }
    }
}
