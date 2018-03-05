// https://www.interviewbit.com/courses/programming/topics/arrays/problems/n3-repeat-number/
// 

public class Solution {
    // DO NOT MODIFY THE LIST
    public int repeatedNumber(final List<Integer> a)
    {
        HashMap<Integer, Long> numReps = new HashMap<Integer,Long>();
        
        for (int i=0; i<a.size(); i++)
        {
            if (numReps.containsKey(a.get(i)))
            {
                numReps.put(a.get(i), numReps.get(a.get(i))+1);
                
                if (numReps.get(a.get(i))> ((double)a.size())/3.0)
                {
                    return a.get(i);
                }
            }
            else
            {
                numReps.put(a.get(i), new Long(1));
                
                if (numReps.get(a.get(i))> ((double)a.size())/3.0)
                {
                    return a.get(i);
                }
            }
        }
        
        return -1;
    }
}

