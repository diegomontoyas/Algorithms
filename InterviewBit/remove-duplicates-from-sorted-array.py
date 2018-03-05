# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/remove-duplicates-from-sorted-array/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i,j = 0,0

        while i<len(A) and j<len(A):
            while j<len(A) and A[i] == A[j]:
                j+=1
                
            if j<len(A):
                if A[i] != A[j] and j>i+1:
                    A[i+1] = A[j]
                    j+=1
                i+=1
            
        return i+1
