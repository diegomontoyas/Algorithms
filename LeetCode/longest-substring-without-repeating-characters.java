// https://leetcode.com/problems/longest-substring-without-repeating-characters
// 45 ms

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start=0, end=0;
        int[] charCount = new int[128];
        int longest=0;
        
        while(end < s.length()) {
            char currentChar = s.charAt(end);
            charCount[currentChar]++;
            end++;
            
            boolean isValid = charCount[currentChar]<=1;
            
            if(isValid) {
                longest = Math.max(longest, end-start);
            }
            
            while(charCount[currentChar]>1) {
                charCount[s.charAt(start)]--;
                start++;
            }
        }
        
        return longest;
    }
}
