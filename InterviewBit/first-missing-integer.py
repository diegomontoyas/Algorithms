# https://www.interviewbit.com/courses/programming/topics/arrays/problems/first-missing-integer/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        numSwapped = 0
        
        for (i, val) in enumerate(A):
            if val < 0:
                A[numSwapped], A[i] = A[i], A[numSwapped] 
                numSwapped += 1

        for i in range(len(A)):
            A[i] = abs(A[i])

        for (i, val) in enumerate(A[numSwapped:]):
            if val <= len(A) and val != 0:
                A[val-1] = -A[val-1]
            
        for (i, val) in enumerate(A):
            if val >= 0:
                return i+1
        
        return len(A)+1
        
