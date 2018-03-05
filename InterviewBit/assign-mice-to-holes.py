# https://www.interviewbit.com/courses/programming/topics/greedy/problems/assign-mice-to-holes/
# 

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        time = 0
        
        for i in xrange(len(A)):
            time = max(abs(B[i]-A[i]), time)
            
        return time
                
