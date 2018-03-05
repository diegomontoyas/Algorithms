# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/array-3-pointers/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        arrays = [A,B,C]
        i,j,k = 0,0,0
        result = 2147483647
        
        if not (A and B and C): return result
        
        while i<len(A) and j<len(B) and k<len(C):
            maxDiff = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
            result = min(result, maxDiff)

            arrIndex, _ = min(enumerate([A[i], B[j], C[k]]), key=lambda x: x[1])
            if arrIndex == 0: i+=1
            elif arrIndex == 1: j+=1
            else: k+=1

        return result
            
