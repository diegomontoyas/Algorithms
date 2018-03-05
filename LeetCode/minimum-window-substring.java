// https://leetcode.com/problems/minimum-window-substring
// 36 ms

public class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> tMap = freqMap(s,t);

        int minWindowStart = -1, minWindowEnd = -1;
        int charsFoundCount = 0;
        int start=0;

        for(int end=0; end < s.length(); end++) {
            char charAtEnd = s.charAt(end); 
            
            if(tMap.get(charAtEnd) > 0) charsFoundCount++;
            tMap.put(charAtEnd, tMap.get(charAtEnd)-1);

            //Valid window
            while(charsFoundCount == t.length()) {
                
                if(minWindowStart == -1 || end+1-start < minWindowEnd+1-minWindowStart) {
                    minWindowStart = start;
                    minWindowEnd = end;
                }
                
                char charAtStart = s.charAt(start); 
                
                tMap.put(charAtStart, tMap.get(charAtStart)+1);
                if(tMap.get(charAtStart) > 0) charsFoundCount--;
                start++;
            }
        }
        
        if(minWindowStart == -1) return "";
        return s.substring(minWindowStart, minWindowEnd+1);
    }
    
    private HashMap<Character, Integer> freqMap(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i=0; i < s.length(); i++) {
            map.put(s.charAt(i), 0);
        }
        
        for (int i=0; i < t.length(); i++) {
            char c = t.charAt(i);
            if(map.containsKey(c)) map.put(c, map.get(c)+1);
            else map.put(c, 1);
        }
        
        return map;
    }
}
