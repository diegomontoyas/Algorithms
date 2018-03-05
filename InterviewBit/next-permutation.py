# https://www.interviewbit.com/courses/programming/topics/arrays/problems/next-permutation/
# 

class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        if len(A) == 1: return A
    
        i=len(A)-1
        while i>0 and A[i-1]>=A[i]:
            i-=1
            
        if i==0:
            self.reverse(A, 0, len(A))    
        else:    
            l=i-1
            while i<len(A) and A[i]>A[l]:
                i+=1
            
            r=i-1
            A[l], A[r] = A[r], A[l]
            self.reverse(A, l+1, len(A))

        return A
        
    def reverse(self, lst, start, end):
        lst[start:end] = lst[start:end][::-1]
        
