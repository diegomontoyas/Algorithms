// https://www.interviewbit.com/courses/programming/topics/bit-manipulation/problems/number-of-1-bits/
// 

public class Solution {
    public int numSetBits(long a) {
        int count = 0;
        long num = a;
        long last = a;
        long mask = ~0L << 1;
        
        while (num != 0) {
            num &= mask;
            if (num != last) count++;
            last = num;
            mask <<= 1;
        }
        
        return count;
    }
}

