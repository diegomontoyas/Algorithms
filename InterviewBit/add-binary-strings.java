// https://www.interviewbit.com/courses/programming/topics/strings/problems/add-binary-strings/
// 

public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int carry = 0;
        
        for(int i=0; i<Math.max(a.length(), b.length()); i++) {
            int one = (a.length()-1-i >= 0 ? a.charAt(a.length()-1-i) == '1' : false) ? 1:0;
            int two = (b.length()-1-i >= 0 ? b.charAt(b.length()-1-i) == '1' : false) ? 1:0;
            
            int columnSum = one^two^carry;
            result.append(String.valueOf(columnSum));
            
            carry = one+two+carry >= 2 ? 1:0;
        }
        
        if (carry > 0) result.append("1");
        while(result.charAt(result.length()-1) == '0') result.deleteCharAt(result.length()-1);
        
        return result.reverse().toString();
    }
}

