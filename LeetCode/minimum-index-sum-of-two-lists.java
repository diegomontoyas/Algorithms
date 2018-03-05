// https://leetcode.com/problems/minimum-index-sum-of-two-lists
// 26 ms

public class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String, Integer> indices = new HashMap<>();
        for(int i=0; i<list2.length; i++) indices.put(list2[i], i);
        
        int minIndicesSum = Integer.MAX_VALUE;
        ArrayList<String> result = new ArrayList<>(Math.min(list1.length, list2.length));
        
        for(int i=0; i<list1.length; i++) {
            String word = list1[i];
            Integer index = indices.get(word);
            
            if(index != null) {
                if(i+index < minIndicesSum) {
                    result.clear();
                    result.add(word);
                    minIndicesSum = i+index;
                } else if(i+index == minIndicesSum) {
                    result.add(word);
                }
            }
        }
        
        return result.toArray(new String[0]);
    }
}
