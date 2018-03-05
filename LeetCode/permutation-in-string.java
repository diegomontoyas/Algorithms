// https://leetcode.com/problems/permutation-in-string
// 23 ms

public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] map = buildOccMap(s1);
        
        int i=0, j=0;
        while(i<s2.length()-s1.length()+1){
            if(isEmpty(map)) return true;
            
            char c = s2.charAt(j);
            
            if(map[c-'a']==-1) {
                while(i<j) {
                    map[s2.charAt(i)-'a']++;
                    i++;
                }
                
                i++;
                j=i;
                
            } else if(map[c-'a']==0) {
                while(map[c-'a']==0 && i<j) {
                    map[s2.charAt(i)-'a']++;
                    i++;
                }
                
            } else {
                map[c-'a']--;
                j++;
            }
        }
        
        return false;
    }
    
    private boolean isEmpty (int[] map) {
        for(int i : map) if(i>0) return false;
        return true;
    }
    
    private int[] buildOccMap(String s) {
        int[] map = new int[26];
        Arrays.fill(map, -1);

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(map[c-'a']==-1) map[c-'a']=0;
            map[c-'a']++;
        }
        
        return map;
    }
}
