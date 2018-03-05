// https://leetcode.com/problems/top-k-frequent-elements
// 34 ms

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freqMap = buildFreqMap(nums);
        
        TreeMap<Integer, List<Integer>> heap = new TreeMap<>();
        
        for (Integer number : freqMap.keySet()) {
            Integer frequency = freqMap.get(number);
        
            if (heap.containsKey(frequency)) {
                heap.get(frequency).add(number);
            } else {
                heap.put(frequency, new ArrayList(Arrays.asList(number)));
            }
            
            if (heap.size() > k) {
                heap.remove(heap.firstKey());
            }
        }
        
        List<Integer> result = new LinkedList<>();
        
        while (result.size()<k) {
            for(Integer num : heap.pollLastEntry().getValue()) {
                result.add(num);
                if(result.size()==k) break;
            }
        }
        
        return result;
    }
    
    private HashMap<Integer, Integer> buildFreqMap(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) {
            if(map.containsKey(num)) map.put(num, map.get(num)+1);
            else map.put(num, 1);
        }
        
        return map;
    }
}
