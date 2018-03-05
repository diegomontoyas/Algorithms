// https://www.interviewbit.com/courses/programming/topics/binary-search/problems/painters-partition-problem/
// 

public class Solution {
    public int paint(int numPainters, int timeToPaintUnit, ArrayList<Integer> boardSizes) {
        int upper = boardSizes.stream().mapToInt(i -> i.intValue()).sum();
        int lower = 0;
        int maxSizePainterCanPaint = Integer.MAX_VALUE;

        while(lower <= upper) {
            int mid = (upper+lower)/2;
            int paintersNeeded = paintersNeeded(mid, boardSizes);

            if(paintersNeeded != -1 && paintersNeeded <= numPainters) {
                maxSizePainterCanPaint = mid;

                //We may have overestimated the value
                upper = mid-1;
            } else {
                //We can't give each painter a board size less then the max established
                lower = mid+1;
            }
        }

        long answer = ((long)maxSizePainterCanPaint)*((long)timeToPaintUnit);
        return (int)(answer%10000003);
    }

    private int paintersNeeded(int maxSize, ArrayList<Integer> boardSizes) {
        int paintersNeeded = 0;
        int currentSum = 0;
        int i=0;

        while(i<boardSizes.size()) {
            int boardSize = boardSizes.get(i);

            if (currentSum + boardSize > maxSize) {
                if (currentSum == 0) return -1;

                paintersNeeded++;
                currentSum = 0;
            } else {
                if (i == boardSizes.size()-1) paintersNeeded++;
                currentSum += boardSize;
                i++;
            }
        }

        return paintersNeeded;
    }
}

