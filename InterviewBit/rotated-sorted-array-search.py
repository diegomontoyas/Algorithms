# https://www.interviewbit.com/courses/programming/topics/binary-search/problems/rotated-sorted-array-search/
# 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if not A: return -1
        
        minIndex = self.findMin(A)
        
        lowerHalf = self.binarySearch(A, B, 0, max(minIndex-1, 0)) 
        if lowerHalf != -1: return lowerHalf
        
        return self.binarySearch(A, B, minIndex, len(A)-1)
        
    def binarySearch(self, A, B, low, upp):
        while low <= upp:
            mid = (low+upp)/2
            
            if A[mid] == B:
                return mid
            elif B > A[mid]:
                low = mid+1
            else:
                upp = mid-1
                
        return -1

    def findMin(self, A):
        if len(A)==1: 
            return 0
        
        low = 0
        upp = len(A) - 1
    
        while low <= upp:
            if A[low] < A[upp]:
                return low
    
            mid = (low + upp) / 2
            prev = (mid-1+len(A))%len(A)
            next = (mid+1)%len(A)
            
            if A[mid] < A[next] and A[mid] < A[prev]:
                return mid
            elif A[mid] >= A[low]:
                low = mid + 1
            else:
                upp = mid - 1
                
