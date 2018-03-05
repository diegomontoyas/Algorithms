// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
// 81 ms

public class Solution {
    public int longestSubstring(String s, int k) {
        int longest = 0;
        
        for (int m=1; m<=buildFreqMap(s).size(); m++) {
            longest = Math.max(longest, longestSubstringUpToMUnique(s, m, k));
        }
        
        return longest;
    }
    
    public int longestSubstringUpToMUnique(String s, int M, int K) {
        int longest = 0;
        HashMap<Character, Integer> freqMap = new HashMap<>();
        int start=0, end=0;
        
        while (end < s.length()) {
            countOccurrence(freqMap, s.charAt(end));
            end++;
                        
            if(_isValid(freqMap, M, K)) {
                // It is a valid configuration
                longest = Math.max(longest, end-start);
            }
            
            while(freqMap.size() > M) {
                removeOccurrence(freqMap, s.charAt(start));
                start++;
            }
        }
        
        return longest;
    }
    
    private boolean _isValid(HashMap<Character, Integer> freqMap, int M, int K) {
        if (freqMap.size() != M) return false;
        
        for(char key : freqMap.keySet()) {
            if (freqMap.get(key) < K) {
                return false;
            }
        }
        
        return true;
    }
    
    private HashMap<Character, Integer> buildFreqMap(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            countOccurrence(map, c);
        }
        
        return map;
    }
    
    private void countOccurrence(HashMap<Character, Integer> map, char c) {
        if(map.containsKey(c)) map.put(c, map.get(c)+1);
        else map.put(c, 1);
    }
    
    private void removeOccurrence(HashMap<Character, Integer> map, char c) {
        if (map.get(c) > 1) map.put(c, map.get(c)-1);
        else map.remove(c);
    }
}
