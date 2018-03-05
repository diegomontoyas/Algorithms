# https://www.interviewbit.com/courses/programming/topics/binary-search/problems/rotated-array/
# 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if len(A)==1: 
            return A[0]
        
        low = 0
        upp = len(A) - 1
    
        while low <= upp:
            if A[low] < A[upp]:
                return A[low]
    
            mid = (low + upp) / 2
            prev = (mid-1+len(A))%len(A)
            next = (mid+1)%len(A)
            
            if A[mid] < A[next] and A[mid] < A[prev]:
                return A[mid]
    
            elif A[mid] >= A[low]:
                low = mid + 1
            else:
                upp = mid - 1

                    
                
