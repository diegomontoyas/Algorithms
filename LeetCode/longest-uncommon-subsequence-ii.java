// https://leetcode.com/problems/longest-uncommon-subsequence-ii
// 13 ms

public class Solution {
    public int findLUSlength(String[] strs) {
        HashMap<String, Integer> counter = new HashMap<>();
        for(String s : strs) counter.put(s, counter.getOrDefault(s, 0)+1);
        
        int longest = -1;
        
        for(int i=0; i<strs.length; i++) { 
            String s = strs[i];
            if(counter.get(s) > 1) continue;
            
            boolean foundSubsequence = false;
            
            for(int j=0; j<strs.length && !foundSubsequence; j++) {
                if(i!=j && isSubsequence(s, strs[j])) {
                    foundSubsequence = true;
                }
            }
            
            if(!foundSubsequence) {
                longest = Math.max(longest, s.length());
            }
        }
        
        return longest;
    }
    
    private boolean isSubsequence(String a, String b) {
        if(a.length() > b.length()) return false;
        
        int j=-1;
        
        for(int i=0; i<a.length(); i++) {
            char c = a.charAt(i);
            j++;
            while(j<b.length() && b.charAt(j) != c) j++;
            if(j==b.length()) return false;
        }
        
        return true;
    }
}
