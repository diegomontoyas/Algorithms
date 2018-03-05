# https://www.interviewbit.com/courses/programming/topics/binary-search/problems/square-root-of-integer/
# 

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        lower = 0
        upper = A
        
        while lower <= upper:
            mid = (lower+upper)/2
            
            if mid**2 == A:
                return mid
            elif mid**2 < A:
                lower = mid+1
            else:
                upper = mid-1
                
        return upper
