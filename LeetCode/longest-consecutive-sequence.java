// https://leetcode.com/problems/longest-consecutive-sequence
// 150 ms

public class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet(Arrays.stream(nums).boxed().collect(Collectors.toList()));
        HashMap<Integer, Integer> memo = new HashMap<>();
        
        int longest=0;
        
        for(int num : nums) {
            int currentLength=1;
            int seqNum = num;
            
            while(set.contains(seqNum+1) && !memo.containsKey(seqNum+1)) {
                currentLength++;
                seqNum++;
            }
            
            if(memo.containsKey(seqNum+1)) currentLength += memo.get(seqNum+1);
            
            memo.put(num, currentLength);
            longest = Math.max(longest, currentLength);
        }
        
        return longest;
    }
}
