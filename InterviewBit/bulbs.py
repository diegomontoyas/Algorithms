# https://www.interviewbit.com/courses/programming/topics/greedy/problems/bulbs/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        flipCount = 0
        
        for i in xrange(len(A)):
            bulbOn = bool(A[i]) if flipCount % 2 == 0 else not bool(A[i])
            if not bulbOn: flipCount += 1
                
        return flipCount
