// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting
// 45 ms

public class Solution {
    public String findLongestWord(String s, List<String> d) {
        String longest = "";
        
        for(String word : d) {
            if(isSubsequence(word, s) && (word.length() > longest.length() 
                                          || (word.length() == longest.length() && word.compareTo(longest) < 0))) {
                longest = word;
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
