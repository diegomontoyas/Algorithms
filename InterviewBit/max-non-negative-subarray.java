// https://www.interviewbit.com/courses/programming/topics/arrays/problems/max-non-negative-subarray/
// 

import java.math.BigInteger;

public class Solution
{
    public ArrayList<Integer> maxset(ArrayList<Integer> a)
    {
        long maxSum=-1;
        int maxSumStart=-1;
        int maxSumEnd=-1;

        int currentStartIndex = -1;
        long currentSum = 0;

        for(int i=0; i<a.size(); i++)
        {
            if(a.get(i) >=0 )
            {
                if (currentStartIndex == -1)
                {
                    currentStartIndex = i;
                    currentSum = 0;
                }
                currentSum += a.get(i);

                if (i == a.size()-1)
                {
                    if (currentSum > maxSum
                    || (currentSum == maxSum && (i-currentStartIndex)>(maxSumEnd-maxSumStart))
                    || (currentSum == maxSum && (i-currentStartIndex)==(maxSumEnd-maxSumStart) && currentStartIndex>maxSumStart))
                    {
                        maxSum = currentSum;
                        maxSumStart = currentStartIndex;
                        maxSumEnd = i;
                        currentStartIndex = -1;
                        currentSum = -1;
                    }
                }
            }
            else if (currentStartIndex != -1)
            {
                if (currentSum > maxSum
                || (currentSum == maxSum && (i-currentStartIndex)>(maxSumEnd-maxSumStart))
                || (currentSum == maxSum && (i-currentStartIndex)==(maxSumEnd-maxSumStart) && currentStartIndex>maxSumStart))
                {
                    maxSum = currentSum;
                    maxSumStart = currentStartIndex;
                    maxSumEnd = i-1;
                }

                currentStartIndex = -1;
                currentSum = -1;
            }
        }

        if (maxSumStart == -1)
        {
            return new ArrayList<Integer>();
        }

        ArrayList ret = new ArrayList();
        for (int i = maxSumStart; i <= maxSumEnd; i++)
        {
            ret.add(a.get(i));
        }
        return ret;
    }
}

