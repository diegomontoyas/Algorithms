// https://www.interviewbit.com/courses/programming/topics/math/problems/excel-column-number/
// 

public class Solution {
    public int titleToNumber(String a) 
    {
        int num = 0;

        for (int i = 0; i < a.length(); i++)
        {
            char c = a.charAt(i);        
            num += charToNumber(c)*Math.pow(26, a.length()-i-1) ;
        }

        return num;
    }
    
    public int charToNumber (char c)
    {
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(c)+1;
    }
}

