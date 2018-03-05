// https://www.interviewbit.com/courses/programming/topics/arrays/problems/find-duplicate-in-array/
// 

public class Solution {
    // DO NOT MODIFY THE LIST
    public int repeatedNumber(final List<Integer> a) 
    {
        int[] ni = new int[a.size()];
        
        for (int i=0; i<a.size(); i++)
        {
            ni[a.get(i)]++;
            
            if (ni[a.get(i)]>1)
            {
                return a.get(i);
            }
        }
        
        return 0;
    }
}

