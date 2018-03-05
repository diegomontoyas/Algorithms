// https://leetcode.com/problems/longest-uncommon-subsequence-i
// 3 ms

public class Solution {
    public int findLUSlength(String a, String b) {
        if(a.length() != b.length()) return Math.max(a.length(), b.length());
        return a.equals(b) ? -1 : a.length();
    }
}
