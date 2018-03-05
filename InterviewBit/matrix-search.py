# https://www.interviewbit.com/courses/programming/topics/binary-search/problems/matrix-search/
# 

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        
        def binarySearch(S, B, searchRow):
            lower = 0
            upper = len(S)-1
        
            while lower <= upper:
                mid = (lower+upper)/2
                
                if searchRow:
                    if S[mid][0] <= B and B <= S[mid][len(S[mid])-1]:
                        return S[mid]
                    elif B < S[mid][0]:
                        upper = mid-1
                    else:
                        lower = mid+1
                    
                else:
                    if S[mid] == B:
                        return 1
                    elif B < S[mid]:
                        upper = mid-1
                    else:
                        lower = mid+1
            
            return None if searchRow else 0
            
        row = binarySearch(A, B, searchRow=True)
        if row is None: return 0
        return binarySearch(row, B, searchRow=False)
                    
                
