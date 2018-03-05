// https://leetcode.com/problems/intersection-of-two-arrays-ii
// 81 ms

public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> result = new ArrayList<>();
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num : nums1) {
            if(map.containsKey(num)) map.put(num, map.get(num)+1);
            else map.put(num, 1);
        }
        
        for(int num : nums2) {
            if(map.containsKey(num) && map.get(num) > 0) {
                map.put(num, map.get(num)-1);
                result.add(num);
            }
        }
        
        return result.stream().mapToInt(i->i).toArray();
    }
}
