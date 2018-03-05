// https://www.interviewbit.com/courses/programming/topics/arrays/problems/add-one-to-number/
// 

public class Solution {
    public ArrayList<Integer> plusOne(ArrayList<Integer> a) 
    {
        int number = 0;
        int carry = 0;
        
        if (a.size()>1)
        {
            for (int i=0; i<a.size(); i++)
            {
                if (a.get(i)==0)
                {
                    a.remove(i);
                    i--;
                }
                else
                {
                    break;
                }
            }
        }
        
        for (int i=a.size()-1; i>=0; i--)
        {
            int toSet = (a.get(i)+ (i==a.size()-1? 1:carry))%10;
            
            carry =0;
            
            if (toSet==0) carry=1;
            
            a.set(i, toSet);
            
            if (carry==0) {break;}
        }
        
        if (carry==1) { a.add(0, 1); }
        
        return a;
    }
}

