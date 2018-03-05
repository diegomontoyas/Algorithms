# https://www.interviewbit.com/courses/programming/topics/two-pointers/problems/remove-duplicates-from-sorted-array-ii/
# 

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        for j in xrange(len(A)):
            if j < len(A)-1 and A[j] == A[j+1] and i>0 and A[i-1] == A[j+1]:
                continue

            A[i] = A[j]
            i+=1
        return i
                
                
                
