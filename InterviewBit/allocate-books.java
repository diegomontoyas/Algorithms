// https://www.interviewbit.com/courses/programming/topics/binary-search/problems/allocate-books/
// 

public class Solution {
    public int books(ArrayList<Integer> bookLengths, int numStudents) {
        if (numStudents > bookLengths.size()) return -1;
        
        int upper = bookLengths.stream().mapToInt(i -> i.intValue()).sum();
        int lower = 0;
        int result = -1;

        while(lower <= upper) {
            int mid = (upper+lower)/2;
            int studentsNeeded = studentsNeeded(mid, numStudents, bookLengths);

            if(studentsNeeded != -1 && studentsNeeded <= numStudents) {
                result = mid;

                //We may have overestimated the value
                upper = mid-1;
            } else {
                //We can't give each student a number of pages less then the max established
                lower = mid+1;
            }
        }

        return result;
    }

    private int studentsNeeded(int maxPages, int numStudents, ArrayList<Integer> bookLengths) {
        int studentsCovered = 0;
        int currentSum = 0;
        int i=0;

        while(i<bookLengths.size()) {
            int bookLength = bookLengths.get(i);

            if (currentSum + bookLength > maxPages) {
                if (currentSum == 0) return -1;

                studentsCovered++;
                currentSum = 0;
            } else {
                if (i == bookLengths.size()-1) studentsCovered++;
                currentSum += bookLength;
                i++;
            }
        }

        return studentsCovered;
    }
}

