// https://www.interviewbit.com/courses/programming/topics/arrays/problems/set-matrix-zeros/
// 

public class Solution {
    public void setZeroes(ArrayList<ArrayList<Integer>> a) 
    {
        HashSet<Integer> pointsX = new HashSet<Integer>();
        HashSet<Integer> pointsY = new HashSet<Integer>();
        
        for (int i=0; i<a.size(); i++)
        {
            for (int j=0; j<a.get(i).size(); j++)
            {
                if (a.get(i).get(j) == 0)
                {
                    pointsX.add(j);
                    pointsY.add(i);
                }
            }
        }
        
        for (int i=0; i<a.size(); i++)
        {
            if (pointsY.contains(i))
            {
                for (int j=0; j<a.get(i).size(); j++)
                {
                    a.get(i).set(j, 0);
                }
            }
        }
        
        for (int j=0; j<a.get(0).size(); j++)
        {
            if (pointsX.contains(j))
            {
                for (int i=0; i<a.size(); i++)
                {
                    a.get(i).set(j, 0);
                }
            }
        }
    }
}

