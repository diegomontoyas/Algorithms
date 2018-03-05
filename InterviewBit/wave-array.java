// https://www.interviewbit.com/courses/programming/topics/arrays/problems/wave-array/
// 

public class Solution 
{
    public ArrayList<Integer> wave(ArrayList<Integer> a) 
    {
        Collections.sort(a);
      
        for (int i=0; i<a.size(); i+=2)
        {
           if (i<a.size()-1) { Collections.swap(a, i, i+1); }
        }
        
        return a;
    }
}

