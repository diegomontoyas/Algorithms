# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/merge-two-sorted-lists-ii/
# 

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        
        i,j = 0,0
        while i<len(A) and j<len(B):
            if A[i] < B[j]:
                i+=1
            else:
                A.insert(i, B[j])
                j+=1
                
        A.extend(B[j:])
        return A
            
