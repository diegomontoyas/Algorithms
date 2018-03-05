// https://leetcode.com/problems/max-points-on-a-line
// 76 ms

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
    public int maxPoints(Point[] points) {
        Arrays.sort(points, (p1, p2) -> {
            if (p1.x != p2.x) return Integer.compare(p1.x, p2.x);
            return Integer.compare(p1.y, p2.y);
        });
        
        if (points.length == 0) return 0;
        if (points.length == 1) return 1;
        
        int maxCount = 2;
        int equal = 1;
        
        for (int i=0; i<points.length; i++) {
            if(i+1<points.length && points[i].x == points[i+1].x && points[i].y == points[i+1].y) {
                equal++;
                maxCount = Math.max(maxCount, equal);
                continue;
            }
            
            for (int j=i+1; j<points.length; j++) {
                
                int count = 1+equal;
                for (int k=j+1; k<points.length; k++) {
                    
                    if (areAligned(points[i], points[j], points[k])) {
                        count++;
                    }
                }
                
                maxCount = Math.max(maxCount, count);
            }
            
            equal = 1;
        }
        
        return maxCount;
    }
    
    private boolean areAligned(Point p1, Point p2, Point p3) {
        
        long dxc = p1.x - p2.x;
        long dyc = p1.y - p2.y;
        
        long dxl = p3.x - p2.x;
        long dyl = p3.y - p2.y;
        
        long cross = dxc * dyl - dyc * dxl;
        return cross == 0;
    }
}
