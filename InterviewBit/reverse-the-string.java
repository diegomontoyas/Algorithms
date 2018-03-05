// https://www.interviewbit.com/courses/programming/topics/strings/problems/reverse-the-string/
// 

public class Solution {
    public String reverseWords(String a) {
        if (a.length()==1) return a;
        
        StringBuilder response = new StringBuilder(a.length());
        Integer wordEnd = null;
        
        for(int i=a.length()-1; i>=0; i--) {
            char c = a.charAt(i);
            
            if((c == ' ' || i==0) && wordEnd != null) {
                if(i==0 && c != ' ') response.append(" ");
                response.append(a.substring(i, wordEnd+1));
                wordEnd = null;
                
            } else if (c != ' ' && wordEnd == null) {
                wordEnd = i;
                if (i==0) response.append(" " + a.charAt(i));
            }
        }
        
        if (response.charAt(0) == ' ') response.deleteCharAt(0);
        return response.toString();
    }
}

