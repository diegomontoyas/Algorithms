// https://leetcode.com/problems/student-attendance-record-i
// 10 ms

public class Solution {
    public boolean checkRecord(String s) {
        int numAs=0;
        int maxContLs=0;
        int currentContLs=0;
        
        for(int i=0; i<s.length() && numAs<=1 && maxContLs<=2; i++) {
            char c = s.charAt(i);
            
            if(c == 'A') {
                numAs++;
                currentContLs=0;
            } else if(c == 'L') {
                currentContLs++;
                maxContLs = Math.max(maxContLs, currentContLs);
            } else {
                currentContLs=0;
            }
        }
        
        return numAs<=1 && maxContLs<=2;
    }
}
