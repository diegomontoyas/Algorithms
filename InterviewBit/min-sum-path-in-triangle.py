# https://www.interviewbit.com/courses/programming/topics/dynamic-programming/problems/min-sum-path-in-triangle/
# 

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        if not A: return None
        sumsTriangle = [A[0]]
        
        for i, level in enumerate(A[1:]):
            sums = []
            for j, num in enumerate(level):
                topLevel = sumsTriangle[i]
                topLeft = topLevel[j-1] if j-1 >= 0 else None
                topRight = topLevel[j] if j < len(topLevel) else None
                topSums = [s for s in [topLeft, topRight] if s is not None]
                
                sums.append(min(topSums)+num)
            sumsTriangle.append(sums)
            
        return min(sumsTriangle[-1])
        
